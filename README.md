# 🚀 Projeto Final Python - Instituto Joga Junto 🐍

## 📌 Descrição
Projeto final do módulo de introdução à Python, onde desenvolvemos uma solução para interagir com a **API do Instituto Joga Junto**. O objetivo é demonstrar conhecimentos em:
- Autenticação via API
- Manipulação de JSON
- Versionamento com Git/GitHub
- Boas práticas de código Python

---

## 🌟 Funcionalidades Principais
✅ Criação de usuário na API  
✅ Autenticação segura via endpoint de login  
✅ Armazenamento estruturado da resposta JSON  
✅ Documentação clara para futuras contribuições  

---

## 🛠️ Comece Aqui
### Passo a passo da API
1. **Criar usuário**  
   ```python
   import requests

   url = "https://desafiopython.jogajuntoinstituto.org/api/users/"
   data = {
       "username": "seu_usuario",
       "password": "sua_senha",
       "email": "email@example.com"
   }
   response = requests.post(url, json=data)

url_login = "http://desafiopython.jogajuntoinstituto.org/api/users/login/"
credentials = {
    "username": "seu_usuario",
    "password": "sua_senha"
}
login_response = requests.post(url_login, json=credentials)
with open('auth_data.json', 'w') as file:
    json.dump(login_response.json(), file)


---

### **4. Prazos e Avisos**
```markdown
---

## 📅 Prazos Importantes
| Data       | Evento                      |
|------------|-----------------------------|
| 30/04/2024 | Apresentação do projeto ⏱️ |
| 10/07/2024 | Entrega final no GitHub 📤 |

> [!WARNING]  
> Lembre-se de fazer upload do JSON de resposta para o repositório!

---

## 🎥 Apresentação
**Requisitos:**  
- 15 minutos de apresentação  
- Compartilhamento de tela com VS Code 🖥️  
- Vídeo de backup gravado (recomendado) 🎬  
- Todos devem estar prontos para responder perguntas ❓

---

## 🤝 Contribuidores
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Edcleryton">
        <img src="https://github.com/Edcleryton.png" width="50px" alt="Edcleryton"/>
      </a>
      <br />
      <a href="https://github.com/Edcleryton">Edcleryton</a>
    </td>
    <td align="center">
      <a href="https://github.com/daniloMelin">
        <img src="https://github.com/daniloMelin.png" width="50px" alt="Danilo Melin"/>
      </a>
      <br />
      <a href="https://github.com/daniloMelin">Danilo Melin</a>
    </td>
    <td align="center">
      <a href="https://github.com/Priest-San">
        <img src="https://github.com/Priest-San.png" width="50px" alt="Priest-San"/>
      </a>
      <br />
      <a href="https://github.com/Priest-San">Priest-San</a>
    </td>
  </tr>
</table>
