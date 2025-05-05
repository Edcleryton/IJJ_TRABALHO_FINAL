import requests
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')
# URL do endpoint para login
url_login = "http://desafiopython.jogajuntoinstituto.org/api/users/login/"

# Dados para login
dados_login = {
    "email": "@teste.com",
    "password": "123456789"
}

# Enviar requisição POST
resposta = requests.post(url_login, json=dados_login)

dados_resposta = resposta.json()
json_str = json.dumps(dados_resposta)


# Grava cada bloco JSON formatado com indentação, separando com linha em branco
with open("resposta_login.json", "a", encoding="utf-8") as arquivo:
    logs = {
        "status_code": resposta.status_code,
        "body":        dados_resposta
    }
    arquivo.write(json.dumps(logs, ensure_ascii=False, indent=4))
    arquivo.write("\n\n") 
    
# Exibir mensagem de sucesso ou falha
if resposta.status_code == 200:
    print("\u2705 Login bem-sucedido! Resposta salva em 'resposta_login.json'.")
else:
    print("\u274c Falha no login. Resposta salva em 'resposta_login.json'.")



