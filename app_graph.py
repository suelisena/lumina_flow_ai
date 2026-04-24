import os
from typing import TypedDict, List
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, END
from langchain_core.messages import BaseMessage, ToolMessage, SystemMessage
from tools import save_lead_to_db, list_all_leads

load_dotenv()

class AgentState(TypedDict):
    messages: List[BaseMessage]

llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0)
tools = [save_lead_to_db, list_all_leads]
llm_with_tools = llm.bind_tools(tools)

def call_model(state: AgentState):
    messages = state['messages'][-5:]
    sys_msg = SystemMessage(content="Você é o Agente LuminaFlow. "
        "REGRA DE OURO: Antes de usar a ferramenta 'save_lead_to_db', você DEVE ter: "
        "Nome, E-mail, Empresa e Interesses. "
        "Se o usuário não forneceu algum desses 4 dados, NÃO invente. "
        "Apenas responda educadamente pedindo a informação que falta.")
    response = llm_with_tools.invoke([sys_msg] + messages)
    return {"messages": [response]}

def call_tools(state: AgentState):
    last_message = state['messages'][-1]
    tool_messages = []
    
  
    if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
        tool_call = last_message.tool_calls[0]
        print(f"🛠️ EXECUTANDO APENAS UMA VEZ: {tool_call['name']}")
        
        if tool_call['name'] == "save_lead_to_db":
            result = save_lead_to_db.invoke(tool_call['args'])
        elif tool_call['name'] == "list_all_leads":
            result = list_all_leads.invoke(tool_call['args'])
        
        tool_messages.append(ToolMessage(content=str(result), tool_call_id=tool_call['id']))
            
    return {"messages": tool_messages}

def should_continue(state: AgentState):
    last_message = state['messages'][-1]
  
    if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
        return "continue"
    return "end"

# --- MONTAGEM DO GRAFO ---
workflow = StateGraph(AgentState)
workflow.add_node("agent", call_model)
workflow.add_node("action", call_tools)
workflow.set_entry_point("agent")


workflow.add_conditional_edges("agent", should_continue, {"continue": "action", "end": END})

workflow.add_edge("action", END) 

app = workflow.compile()