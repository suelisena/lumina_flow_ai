import os
from pymongo import MongoClient
from dotenv import load_dotenv
from langchain_core.tools import tool

load_dotenv()


client = MongoClient(os.getenv("MONGO_URI"))
db = client["suelissena_db_user"]
leads_collection = db["leads"]

@tool
def save_lead_to_db(name: str, email: str, company: str, interests: str):
    """Salva os dados de um potencial cliente (lead) no banco de dados MongoDB."""
    try:
        lead_data = {
            "name": name,
            "email": email,
            "company": company,
            "interests": interests,
            "status": "Novo"
        }
        result = leads_collection.insert_one(lead_data)
        return f"✅ Lead {name} salvo com sucesso! "
    except Exception as e:
        return f"❌ Erro ao salvar no banco: {e}"

@tool
def list_all_leads():
    """Lista os últimos leads cadastrados no sistema."""
    try:
        leads = list(leads_collection.find().sort("_id", -1))
        if not leads:
            return "Nenhum lead encontrado."
        
        output = "📋 Lista de Leads:\n"
        for l in leads:
            output += f"- {l.get('name', 'Nome não disponível')} ({l.get('email', 'Email não disponível')}) | Empresa: {l.get('company', 'Empresa não disponível')}\n"
        return output
    except Exception as e:
        return f"❌ Erro ao listar leads: {e}"