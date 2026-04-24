# 🤖 LuminaFlow AI — Gestão Inteligente de Leads

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB">
  <img src="https://img.shields.io/badge/LangChain-121212?style=for-the-badge&logo=chainlink&logoColor=white" alt="LangChain">
  <img src="https://img.shields.io/badge/Groq-f34f29?style=for-the-badge&logo=fastapi&logoColor=white" alt="Groq">
</p>

O **LuminaFlow AI** é um ecossistema inteligente que integra Agentes de IA (LLMs) com bancos de dados NoSQL e dashboards analíticos. A ferramenta transforma conversas em linguagem natural em dados estruturados, permitindo o gerenciamento e a visualização de leads de forma automatizada.

---

## 📌 Sumário
- [🚀 Visão Geral](#-visão-geral)
- [🛠️ Tecnologias Utilizadas](#️-tecnologias-utilizadas)
- [🏗️ Arquitetura do Sistema](#️-arquitetura-do-sistema)
- [📊 Funcionalidades](#-funcionalidades)
- [⚙️ Instalação e Configuração](#️-instalação-e-configuração)
- [👩‍💻 Autora](#-autora)

---

## 🚀 Visão Geral
Este projeto foi desenvolvido para demonstrar a viabilidade de Agentes Reativos em fluxos de trabalho empresariais. O LuminaFlow utiliza o modelo **Llama 3 (via Groq)** para interpretar intenções do usuário, cadastrar informações no **MongoDB Atlas** e renderizar métricas em um Dashboard dinâmico com **Chart.js**.

---

## 🛠️ Tecnologias Utilizadas
- **IA & NLP**: LangChain, Groq API (Llama 3).
- **Back-end**: Python, Flask.
- **Banco de Dados**: MongoDB Atlas (NoSQL).
- **Front-end**: Jinja2, Bootstrap 5, Chart.js.
- **Saneamento de Dados**: Regex e processamento de strings em Python.

---

## 🏗️ Arquitetura do Sistema
O sistema opera em um fluxo de quatro etapas:
1. **Chat Interativo**: O usuário insere dados brutos (ex: "Cadastre o Ricardo da Brasil Logística").
2. **Processamento LLM**: O Agente identifica a ferramenta (tool) de cadastro e extrai os campos necessários.
3. **Persistência**: O dado é sanitizado e persistido no MongoDB.
4. **Visualização**: A rota do Dashboard executa uma agregação e exibe a distribuição de leads em tempo real.

---

## 📊 Funcionalidades
- [x] **Cadastro via IA**: Reconhecimento de nomes, empresas e interesses em linguagem natural.
- [x] **Dashboard em Tempo Real**: Visualização de volumetria total e distribuição por empresa.
- [x] **Interface Responsiva**: Dashboard adaptável para diferentes resoluções.
- [x] **Estratégia No-Cache**: Garantia de integridade dos dados visualizados.

### 📸 Preview
<p align="center">
  <img src="caminho/para/seu/print_dashboard.png" width="800" alt="Dashboard LuminaFlow">
</p>

---

## ⚙️ Instalação e Configuração

### Pré-requisitos
- Python 3.10+
- Conta no MongoDB Atlas
- Chave de API do Groq

### Passo a Passo
1. Clone o repositório:
   ```bash
   git clone [https://github.com/seu-usuario/luminaflow-ai.git](https://github.com/seu-usuario/luminaflow-ai.git)
   cd luminaflow-ai
   
2. Crie e ative o ambiente virtual:

python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

3. Instale as dependências:
pip install -r requirements.txt

4. Configure as variáveis de ambiente (.env):
GROQ_API_KEY=sua_chave_aqui
MONGO_URI=sua_uri_do_mongodb

6. Execute a aplicação:
python app.py

👩‍💻 Autora
Sueli Sena Systems Analyst Specialist | Full Stack Developer | AI Enthusiast
