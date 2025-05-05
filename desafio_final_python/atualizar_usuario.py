import requests
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

user_id = input("Digite o ID do usuário que deseja atualizar: ")
url = f"https://desafiopython.jogajuntoinstituto.org/api/users/{user_id}"

novos_dados = {
    "email":    "novo_email@teste.com",
    "username": "NovoNomeUsuario"
}

resposta = requests.put(url, json=novos_dados)

try:
    dados_resposta = resposta.json()
except json.JSONDecodeError:
    dados_resposta = {"mensagem": "Resposta não é JSON válido", "raw": resposta.text}

with open("resposta_atualizar_usuario.json", "a", encoding="utf-8") as arquivo:
    log = {
        "status_code": resposta.status_code,
        "body":        dados_resposta
    }
    arquivo.write(json.dumps(log, ensure_ascii=False, indent=4))
    arquivo.write("\n\n")

if resposta.status_code == 200:
    print("✅ Usuário atualizado com sucesso! Log salvo em 'resposta_atualizar_usuario.json'.")
elif resposta.status_code == 404:
    print("❌ Usuário não encontrado. Log salvo em 'resposta_atualizar_usuario.json'.")
else:
    print(f"❌ Falha ao atualizar usuário. Log salvo em 'resposta_atualizar_usuario.json'.")
