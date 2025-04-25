import requests
import json
from datetime import datetime

# URL dos endpoints
URL_CRIAR_USUARIO = "https://desafiopython.jogajuntoinstituto.org/api/users/"
URL_LOGIN = "http://desafiopython.jogajuntoinstituto.org/api/users/login/"

# Dados para criar usuário
dados_criar_usuario = {
    "username": "userteste",
    "email": "teste@teste.com",
    "password": "123456789",
    "phone": "12345678901",
    "address": "123 Main St, City, Country",
    "cpf": "003.456.789-00"
}

# Dados para login
dados_login = {
    "email": "teste@teste.com",
    "password": "123456789"
}

# Função para registrar logs
def registrar_log(tipo, endpoint, status_code, sucesso):
    log = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "tipo": tipo,
        "endpoint": endpoint,
        "status_code": status_code,
        "sucesso": sucesso
    }
    with open("logs.json", "a") as arquivo:
        json.dump(log, arquivo)
        arquivo.write("\n")  # Cada log em uma linha

# Passo 1: Criar usuário
try:
    response_criar_usuario = requests.post(URL_CRIAR_USUARIO, json=dados_criar_usuario)
    sucesso_criar = response_criar_usuario.status_code == 201
    registrar_log("POST", URL_CRIAR_USUARIO, response_criar_usuario.status_code, sucesso_criar)
except Exception as e:
    registrar_log("POST", URL_CRIAR_USUARIO, 0, False)  # Status 0 indica erro de conexão
    exit()

# Passo 2: Fazer login
try:
    response_login = requests.post(URL_LOGIN, json=dados_login)
    sucesso_login = response_login.status_code == 200
    registrar_log("POST", URL_LOGIN, response_login.status_code, sucesso_login)
except Exception as e:
    registrar_log("POST", URL_LOGIN, 0, False)
    exit()

# Salvar resposta do login (opcional)
with open("resposta_login.json", "w") as arquivo:
    json.dump(response_login.json(), arquivo, indent=4)