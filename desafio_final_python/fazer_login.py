import requests
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')
# URL do endpoint para login
url_login = "http://desafiopython.jogajuntoinstituto.org/api/users/login/"

# Dados para login
dados_login = {
    "email": "danilo.teste@teste.com",
    "password": "123456789"
}

# Enviar requisição POST
resposta = requests.post(url_login, json=dados_login)

dados_resposta = resposta.json()
json_str = json.dumps(dados_resposta)

with open("resposta_login.json", "w") as arquivo:
    arquivo.write(json_str)

# Exibir mensagem de sucesso ou falha
if resposta.status_code == 200:
    print("\u2705 Login bem-sucedido! Resposta salva em 'resposta_login.json'.")
else:
    print(f"\u274c Falha no login. Resposta salva em 'resposta_login.json'.")

# Verificar status e exibir resultado
# if resposta.status_code == 200:
#     print("\u2705 Login bem-sucedido! Status Code: {response.status_code}")
#     print("Resposta da API:", resposta.json())

#     dados_resposta = resposta.json()
#     json_str = json.dumps(dados_resposta)
#     with open("resposta_login.json", "w") as arquivo:
#         arquivo.write(json_str)
#     print("\u2705 Resposta do login salva em 'resposta_login.json'.")

# else:
#     print(f"\u274c Falha no login. Status Code: {resposta.status_code}")
#     print("Resposta da API:", resposta.json())

