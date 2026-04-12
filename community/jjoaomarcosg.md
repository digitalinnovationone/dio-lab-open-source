### Olá, eu sou João Marcos 👋
- Análise e Desenvolvimento de Sistemas | Faculdade Estácio

- Sou estudante iniciante de Python e estou fazendo minha primeira contribuição em Open Source!

- Iniciado em Python aqui pelo Bootcamp

## Contato
- LinkedIn: [www.linkedin.com/in/joão-marcos-gomes-63654516b]
- GitHub: [https://github.com/jjoaomarcosg]

## Mini Script de Boas-vindas em Python

```python
# Fizste um mini script de boas-vindas para mostrar conceitos básicos de Python que aprendi até agora.
# Utiliza input, print e estruturas condicionais if/elif/else

# Aqui pergunta o nome do usuário
nome = input("Qual o seu nome? ")

# Pergunta se quer ver uma mensagem de boas-vindas
resposta = input("Você quer ver uma mensagem de boas-vindas? (sim/não) ")

# Estrutura condicional para responder de acordo com a escolha do usuário
if resposta.lower() == "sim":
    print(f"Bem-vindo(a) ao projeto, {nome}!")
elif resposta.lower() == "não":
    print(f"Tudo bem, {nome}, talvez outra hora!")
else:
    print("Opção inválida, tente novamente.")
