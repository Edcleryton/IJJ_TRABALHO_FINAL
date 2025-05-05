import requests
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# URL base do endpoint
user_id = input("Digite o ID do usuário que deseja excluir: ")
url = f"https://desafiopython.jogajuntoinstituto.org/api/users/{user_id}"

# Enviar requisição DELETE
resposta = requests.delete(url)

# Tentar converter resposta em JSON
try:
    dados_resposta = resposta.json()
except json.JSONDecodeError:
    dados_resposta = {"mensagem": "Resposta não é JSON válido", "raw": resposta.text}

# Gravar resposta formatada no arquivo com indentação e separação
with open("resposta_excluir_usuario.json", "a", encoding="utf-8") as arquivo:
    log = {
        "status_code": resposta.status_code,
        "body": dados_resposta
    }
    arquivo.write(json.dumps(log, ensure_ascii=False, indent=4))
    arquivo.write("\n\n")  # quebra extra para separar blocos

# Exibir resultado
if resposta.status_code == 204:
    print("\u2705 Usuário excluído com sucesso! Log salvo em 'resposta_excluir_usuario.json'.")
else:
    print("\u274c Falha ao excluir usuário. Log salvo em 'resposta_excluir_usuario.json'.")
