import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from tools import save_lead_to_db, list_all_leads


load_dotenv()

def initialize_agent():
 
    llm = ChatGroq(
        temperature=0, 
        model_name="llama-3.3-70b-versatile",
        groq_api_key=os.getenv("GROQ_API_KEY")
    )
    
   
    tools = [save_lead_to_db, list_all_leads]
    
   
    llm_with_tools = llm.bind_tools(tools)
    return llm_with_tools

def run_agent(user_query):
    llm = initialize_agent()
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", """Você é um Agente de Operações da LuminaFlow AI.
        Sua função é gerenciar leads de consultoria. 
        Se o usuário fornecer dados de contato, use a ferramenta 'save_lead_to_db'.
        Se o usuário pedir para ver os leads, use 'list_all_leads'.
        Sempre responda de forma profissional em Português."""),
        ("user", "{input}")
    ])
    
    chain = prompt | llm
    
    try:
        
        response = chain.invoke({"input": user_query})
        
        #
        if response.tool_calls:
            print("\n🛠️ O Agente decidiu usar uma ferramenta!")
            for tool_call in response.tool_calls:
                print(f"Chamando: {tool_call['name']} com os dados: {tool_call['args']}")
                
               
                if tool_call['name'] == "save_lead_to_db":
                    res = save_lead_to_db.invoke(tool_call['args'])
                    print(res)
                elif tool_call['name'] == "list_all_leads":
                    res = list_all_leads.invoke(tool_call['args'])
                    print(res)
        else:
            print("\n🤖 Resposta da IA:\n")
            print(response.content)
            
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    
    print("--- Teste 1: Salvar Lead ---")
    run_agent("Olá, meu nome é Sueli, meu e-mail é sueli@exemplo.com. Trabalho na empresa TechInova e tenho interesse em projetos de Inteligência Artificial.")
    
   
    print("\n--- Teste 2: Listar Leads ---")
    run_agent("Pode me mostrar quais leads temos cadastrados?")