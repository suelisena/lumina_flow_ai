from flask import Flask, render_template, request, jsonify
from app_graph import app as agent_app
from langchain_core.messages import HumanMessage
from flask import render_template, make_response
from tools import list_all_leads
from collections import Counter
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"error": "Mensagem vazia"}), 400
    inputs = {"messages": [HumanMessage(content=user_message)]}
    result = agent_app.invoke(inputs)
    final_response = result['messages'][-1].content
    return jsonify({"response": final_response})


@app.route('/dashboard')
def dashboard():
    try:
        
        raw_data = list_all_leads.invoke({})
        leads_extraidos = []
        
        
        if isinstance(raw_data, str):
           
            padrao = r"-\s*([^(\n|]+).*?Empresa:\s*([^|\n]+)"
            matches = re.findall(padrao, raw_data)
            
            for m in matches:
                leads_extraidos.append({
                    "name": m[0].strip(),
                    "company": m[1].strip()
                })
        else:
            leads_extraidos = raw_data

       
        empresas = [l.get('company', 'Outras') for l in leads_extraidos]
        stats = dict(Counter(empresas))
        
        
        response = make_response(render_template('dashboard.html', 
                               leads=leads_extraidos, 
                               total=len(leads_extraidos), 
                               labels=list(stats.keys()), 
                               values=list(stats.values())))
        
       
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        
        return response

    except Exception as e:
        print(f"Erro no Dashboard: {e}")
        return "Erro ao carregar os dados", 500

if __name__ == '__main__':
    app.run(debug=True)