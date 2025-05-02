# 🧪 Testes Manuais - Projeto Final Python 🐍

> **Objetivo:** Documentar os testes manuais realizados no projeto para validar as funcionalidades e identificar inconsistências.

---

## 📋 Índice

- [Teste 1: Requisitos de Senha](#teste-1-requisitos-de-senha)
- [Teste 2: Validação de CPF](#teste-2-validação-de-cpf)
- [Teste 3: Status Code de Erro para Dados Duplicados](#teste-3-status-code-de-erro-para-dados-duplicados)
- [Teste 4: Aceitação de Caracteres Especiais e Emojis](#teste-4-aceitação-de-caracteres-especiais-e-emojis)
- [Resultados dos Testes](#resultados-dos-testes)
- [Observações Finais](#observações-finais)

---

## 🧪 Teste 1: Requisitos de Senha

**Objetivo:** Verificar se a API aceita senhas com 8 caracteres, conforme especificado.

| **Passo** | **Ação** | **Resultado Esperado** | **Resultado Obtido** | **Status** |
|----------|------------|------------------------|----------------------|------------|
| 1        | Enviar requisição com senha de 8 caracteres (ex.: `12345678`). | Usuário criado com sucesso. | Falha ao criar usuário. Status Code: `400`. | ❌ Falhou |
| 2        | Enviar requisição com senha de 9 caracteres (ex.: `123456789`). | Usuário criado com sucesso. | Sucesso. Status Code: `201`. | ✅ Passou |

---

## 🧪 Teste 2: Validação de CPF

**Objetivo:** Validar se o CPF é único e segue o formato correto (`003.456.789-00`).

| **Passo** | **Ação** | **Resultado Esperado** | **Resultado Obtido** | **Status** |
|----------|------------|------------------------|----------------------|------------|
| 1        | Criar usuário com CPF válido (`003.456.789-00`). | Usuário criado com sucesso. | Sucesso. Status Code: `201`. | ✅ Passou |
| 2        | Criar outro usuário com o mesmo CPF. | Erro de CPF duplicado. | Sucesso. Status Code: `201` (CPF duplicado foi aceito). | ❌ Falhou |
| 3        | Criar usuário com CPF inválido (ex.: letras, emojis, menos de 11 dígitos). | Erro de validação de CPF. | Sucesso. Status Code: `201` (CPF inválido foi aceito). | ❌ Falhou |

---

## 🧪 Teste 3: Status Code de Erro para Dados Duplicados

**Objetivo:** Verificar se a API retorna o status code correto para dados duplicados (`409 Conflict`).

| **Passo** | **Ação** | **Resultado Esperado** | **Resultado Obtido** | **Status** |
|----------|------------|------------------------|----------------------|------------|
| 1        | Criar usuário com email já cadastrado. | Status Code: `409 Conflict`. | Status Code: `400 Bad Request`. | ❌ Falhou |
| 2        | Criar usuário com username já cadastrado. | Status Code: `409 Conflict`. | Status Code: `400 Bad Request`. | ❌ Falhou |

---

## 🧪 Teste 4: Aceitação de Caracteres Especiais e Emojis

**Objetivo:** Validar se a API aceita caracteres especiais e emojis em campos específicos.

| **Passo** | **Ação** | **Resultado Esperado** | **Resultado Obtido** | **Status** |
|----------|------------|------------------------|----------------------|------------|
| 1        | Criar usuário com username contendo emojis (ex.: `João✨`). | Erro: apenas texto alfanumérico permitido. | Sucesso. Status Code: `201`. | ❌ Falhou |
| 2        | Criar usuário com password contendo apenas caracteres especiais (ex.: `!@#$%^&*`). | Sucesso: senha aceita. | Sucesso. Status Code: `201`. | ✅ Passou |
| 3        | Criar usuário com CPF contendo letras (ex.: `abc.def.ghi-jk`). | Erro: CPF deve conter apenas números. | Sucesso. Status Code: `201`. | ❌ Falhou |

---

## 📊 Resultados dos Testes

| **Funcionalidade** | **Total de Testes** | **Passaram** | **Falhas** |
|--------------------|---------------------|--------------|------------|
| Requisitos de Senha | 2                   | 1            | 1          |
| Validação de CPF    | 3                   | 1            | 2          |
| Status Code de Erro  | 2                   | 0            | 2          |
| Caracteres Especiais| 3                   | 1            | 2          |

✅ **Status Final:**  

- **Passaram:** 1 teste (senha com 9 caracteres).  
- **Falharam:** 5 testes (requisitos de senha, validação de CPF, status code 409, caracteres especiais em username e validação de CPF com letras).

---

## 📝 Observações Finais

1. **Requisitos de Senha:**
   - A API exige 8 caracteres para a senha, embora ao realizar o teste criando um usuário, nota-se que o mínimo é 9 caracteres.
   - Isso pode causar confusão para usuários e deve ser corrigido.

2. **Validação de CPF:**
   - A API não valida o formato do CPF e permite cadastro com letras, emojis e CPF duplicado.
   - Isso compromete a integridade dos dados, já que o CPF é um documento único por usuário.

3. **Status Code de Erro:**
   - O status code `400 Bad Request` é usado para erros de validação, mas o correto para conflitos (ex.: email ou username duplicado) seria `409 Conflict`.
   - Atualize as mensagens de erro para refletir o status correto.

4. **Caracteres Especiais e Emojis:**
   - A API aceita emojis em campos como `username`, o que pode não ser desejado.
   - Campos como `cpf` e `email` devem ter validações mais rígidas.

---

