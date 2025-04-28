import requests
import sys
sys.stdout.reconfigure(encoding='utf-8')
# URL do endpoint para criar usuário
url_criar_usuario = "https://desafiopython.jogajuntoinstituto.org/api/users/"

# Dados do usuário
dados_criar_usuario = {
    "username": "Danilo_test",
    "email": "danilo.teste@teste.com",
    "password": "123456789",
    "phone": "12345678901",
    "address": "Rua Carlos Gomes 142, São Paulo, Brasil",
    "cpf": "003.460.790-00"
}

# Enviar POST
resposta = requests.post(url_criar_usuario, json=dados_criar_usuario)

# Verificar status e exibir resultado
if resposta.status_code == 201:
    print(f"\u2705 Usuário criado com sucesso!{resposta.status_code}")
    print("Detalhes da resposta:", resposta.json())
else:
    print(f"\u274c Falha ao criar usuário. Status Code: {resposta.status_code}")
    print("Resposta da API:", resposta.json())
    exit()

