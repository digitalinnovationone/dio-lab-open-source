# API REST - Resumo

## O que é?

Uma **API REST** é um padrão de comunicação entre sistemas usando o protocolo **HTTP**. Normalmente, os dados são enviados e recebidos em **JSON**.

---

## Métodos HTTP

| Método | Função |
|--------|--------|
| GET | Buscar dados |
| POST | Criar |
| PUT | Atualizar |
| PATCH | Atualizar parcialmente |
| DELETE | Remover |

---

## Exemplo

### Requisição

```http
GET /usuarios/1
```

### Resposta

```json
{
  "id": 1,
  "nome": "Ana"
}
```

---

## Códigos HTTP

- **200** – OK
- **201** – Criado
- **400** – Requisição inválida
- **404** – Não encontrado
- **500** – Erro interno

---

## CRUD

| Operação | Método |
|----------|--------|
| Create | POST |
| Read | GET |
| Update | PUT/PATCH |
| Delete | DELETE |

---

## Resumo

- REST é um padrão para criação de APIs.
- Utiliza o protocolo HTTP.
- Os dados geralmente são enviados em **JSON**.
- Cada recurso possui uma URL (endpoint).
- Os métodos HTTP definem a operação realizada.
