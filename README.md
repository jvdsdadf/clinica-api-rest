# Clinic API

API REST para um cenário simples de clínica médica, construída com FastAPI + SQLAlchemy + MySQL.

## Por que esse projeto existe
Montei essa API para praticar:
- modelagem básica (CRUD)
- validação com Pydantic
- organização em camadas (rotas → serviços → repositórios)
- integração com MySQL via SQLAlchemy

## O que já existe 
Recurso principal: **Pacientes**
- Criar paciente
- Listar pacientes
- Buscar paciente por id
- Atualizar paciente
- Remover paciente

## Tecnologias usadas
- Python 3.12+
- FastAPI
- SQLAlchemy
- MySQL
- Pydantic
- Uvicorn
- python-dotenv

## Como rodar
1) Clonar e entrar na pasta:

git clone https://github.com/jvdsdadf/clinica-api-rest.git

cd clinica-api-rest/api

Criar venv e instalar:

py -m venv venv
venv\Scripts\activate
py -m pip install -r requirements.txtConfigurar variáveis de ambiente
Crie um arquivo .env (ou use .env.example) com:

DB_HOST=

DB_PORT=

DB_USER=

DB_PASSWORD=

DB_NAME=

Subir a API:

py -m uvicorn app.main:app --reload

Endpoints

Swagger: http://127.0.0.1:8000/docs

Health: http://127.0.0.1:8000/health (Saber se a API está ativa)

Exemplo — Criar paciente

POST / pacientes

Requisição:

{
  "nome": "João da Silva",
  "cpf": "12345678909",
  "dataNascimento": "1998-05-20",
  "telefone": "11999999999",
  "email": "joao@email.com"
}


Resposta:

{
  "id": 1,
  "nome": "João da Silva",
  "cpf": "12345678909",
  "dataNascimento": "1998-05-20",
  "telefone": "11999999999",
  "email": "joao@email.com",
  "createdAt": "2026-01-20T12:00:00Z"
}


