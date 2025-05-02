# 🧪 Testes Manuais

Este documento descreve os testes manuais realizados no script `login.py`.

---

## ✅ Teste 1: Login com Credenciais Válidas

**Objetivo:** Verificar se o login é bem-sucedido com email e senha corretos.

### Passos

1. Execute `login.py` com os dados abaixo:

   ```python
   dados_login = {
       "email": "edcleryton@teste.com",
       "password": "123456789"
   }
   ```

2. Confira se o status code é `200 OK`.
3. Verifique se o arquivo `resposta_login.json` foi criado com o token.

### Resultado Esperado

- Status Code: `200 OK`  
- Arquivo `resposta_login.json` com token válido.

### Resultado Obtido (Teste 4)

✅ Passou / ❌ Falhou (preencha após testar)

---

## ❌ Teste 2: Login com Email ou Senha Incorretos

**Objetivo:** Validar se o script exibe mensagem de erro ao usar credenciais inválidas.

### Passos

1. Execute `login.py` com os dados abaixo:

   ```python
   dados_login = {
       "email": "usuario_errado@teste.com",
       "password": "senha_errada"
   }
   ```

2. Confira se o status code é `401 Unauthorized` ou `400 Bad Request` (conforme resposta da API).
3. Verifique se a mensagem de erro é clara.

### Resultado Esperado

- Status Code: `401` ou `400`  
- Mensagem: `"❌ Falha no login. Credenciais inválidas."`

### Resultado Obtido

✅ Passou / ❌ Falhou (preencha após testar)

---

## 🛑 Teste 3: Login com Campos Obrigatórios Ausentes

**Objetivo:** Verificar como o script lida com campos vazios ou ausentes.

### Passos

1. Execute `login.py` com os dados abaixo:

   ```python
   dados_login = {
       "email": "",
       "password": ""
   }
   ```

2. Confira se o status code é `400 Bad Request`.
3. Verifique se a mensagem de erro é clara.

### Resultado Esperado

- Status Code: `400 Bad Request`  
- Mensagem: `"❌ Falha no login. Campos obrigatórios ausentes."`

### Resultado Obtido

✅ Passou / ❌ Falhou (preencha após testar)

---

### Resultado Obtido

✅ Passou / ❌ Falhou (preencha após testar)

---

## 📂 Teste 4: Salvamento do JSON com Formatação Correta

**Objetivo:** Garantir que o JSON salvo no arquivo `resposta_login.json` esteja formatado corretamente.

### Passos

1. Execute `login.py` com credenciais válidas.
2. Abra `resposta_login.json` e verifique:
   - Se o arquivo tem indentação (`indent=4`).
   - Se caracteres especiais (ex.: emojis) são preservados (`ensure_ascii=False`).

### Resultado Esperado

- Arquivo JSON legível e formatado.

### Resultado Obtido

✅ Passou / ❌ Falhou (preencha após testar)
