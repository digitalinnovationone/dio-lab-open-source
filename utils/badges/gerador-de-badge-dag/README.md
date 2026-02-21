
# Gerador Interativo de Badges para README

Este é um script simples feito em Node.js que permite criar badges personalizados para README de forma interativa, diretamente pelo terminal.

---

## Requisitos

- Node.js versão 14 ou superior
- Pacote `inquirer` (instalado via `npm install inquirer`)

---

## Como executar

1. Instale as dependências:

```
npm install
```

2. Execute o script:

```
node gerador-de-badge.js
```

---

## Como funciona

O programa faz uma sequência de perguntas no terminal:

```
Texto do badge (ex: html, css, javascript)?
> java

Cor (nome ou hex, ex: blue ou #ED8B00)?
> #ED8B00

Estilo (ex: flat, flat-square, for-the-badge)?
> for-the-badge

Logo opcional (ex: html, css, javascript)? (Deixe vazio se não quiser)
> openjdk

Cor do logo (ex: white)? (Deixe vazio se não quiser)
> white

Quer adicionar outro badge?
> n
```

---

## Exemplo de saída gerada (`badges.md`)

```markdown
![java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white)
```

Este código gerado já fica pronto para você copiar e colar no seu README.

---
