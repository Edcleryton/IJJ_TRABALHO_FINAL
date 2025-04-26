import requests

requisicao = requests.get('https://desafiopython.jogajuntoinstituto.org/api/users')

requisicao.encoding = 'utf-8'
requisicao.status_code
requisicao.json()
print(f'equisicao: {requisicao}')
print(f'equisicao.status_code: {requisicao.status_code}')
print(f'requisicao.json(): {requisicao.json()}')