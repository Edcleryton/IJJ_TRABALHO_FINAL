import requests
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# URL base
url_base = "https://desafiopython.jogajuntoinstituto.org/api/users/"

# Entrada do tipo de busca e valor
tipo_busca = input("Olá, bem vindo! Para buscar um usuário digite uma das opç~es a seguir: [id], [email] ou [username]. ").strip().lower()
valor_busca = input(f"Digite o {tipo_busca}: ")

# Montar a URL completa
url_completa = f"{url_base}?{tipo_busca}={valor_busca}"

# Fazer a requisição
response = requests.get(url_completa)

# Processar a resposta
try:
    todos_os_dados = response.json()

    # Se a API retornar uma lista de usuários, filtramos localmente
    if isinstance(todos_os_dados, list):
        usuario_filtrado = None
        if tipo_busca == "id":
            usuario_filtrado = next((u for u in todos_os_dados if str(u.get("id")) == valor_busca), None)
        elif tipo_busca == "email":
            usuario_filtrado = next((u for u in todos_os_dados if u.get("email") == valor_busca), None)
        elif tipo_busca == "username":
            usuario_filtrado = next((u for u in todos_os_dados if u.get("username") == valor_busca), None)

        dados_resposta = usuario_filtrado or {"message": "Usuário não encontrado"}
    else:
        dados_resposta = todos_os_dados

except json.JSONDecodeError:
    dados_resposta = {"raw": response.text}

# Salvar no arquivo
with open("resposta_buscar_usuario.json", "a", encoding="utf-8") as arquivo:
    bloco = {
        "body": dados_resposta
    }
    arquivo.write(json.dumps(bloco, ensure_ascii=False, indent=4))
    arquivo.write("\n\n")