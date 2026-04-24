import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def test_connection():
    try:
        client = MongoClient(os.getenv("MONGO_URI"))
        # Tenta obter informações do servidor
        client.admin.command('ping')
        print("✅ Conexão com o MongoDB Atlas realizada com sucesso!")
    except Exception as e:
        print(f"❌ Erro na conexão: {e}")

if __name__ == "__main__":
    test_connection()