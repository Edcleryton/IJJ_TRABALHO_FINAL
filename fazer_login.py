import requests
import sys
sys.stdout.reconfigure(encoding='utf-8')
# URL do endpoint para login
url_login = "http://desafiopython.jogajuntoinstituto.org/api/users/login/"

# Dados para login
dados_login = {
    "email": "edcleryton@teste.com",
    "password": "123456789"
}

# Enviar requisição POST
response = requests.post(url_login, json=dados_login)

# Verificar status e exibir resultado
if response.status_code == 200:
    print("\u2705 Login bem-sucedido! Status Code: {response.status_code}")
    print("Resposta da API:", response.json())
else:
    print(f"\u274c Falha no login. Status Code: {response.status_code}")
    print("Resposta da API:", response.json())