import requests
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# URL do endpoint para criar usuário
url_criar_usuario = "https://desafiopython.jogajuntoinstituto.org/api/users/"

# Dados do usuário
dados_criar_usuario = {
    "username": "test",
    "email": "teste@teste.com",
    "password": "123456789",
    "phone": "12345678901",
    "address": "Rua Floriano Peixoto 142, Salvador, Brasil",
    "cpf": "003.456.789-00"
}

# Enviar POST
resposta = requests.post(url_criar_usuario, json=dados_criar_usuario)
dados_resposta = resposta.json()

# Gravar resposta formatada no arquivo com indentação e separação
with open("resposta_criar_usuario.json", "a", encoding="utf-8") as arquivo:
    log = {
        "status_code": resposta.status_code,
        "body": dados_resposta
    }
    arquivo.write(json.dumps(log, ensure_ascii=False, indent=4))
    arquivo.write("\n\n")  # quebra extra para separar blocos

# Exibir resultado
if resposta.status_code == 201:
    print("\u2705 Usuário criado com sucesso! Log salvo em 'resposta_criar_usuario.json'.")
else:
    print("\u274c Falha ao criar usuário. Log salvo em 'resposta_criar_usuario.json'.")
