import requests
import json
from datetime import datetime

# URLs dos endpoints
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