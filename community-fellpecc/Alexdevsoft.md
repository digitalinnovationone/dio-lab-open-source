# Alexsandro Almeida

## Sobre Mim

Olá! Meu nome é Alexsandro Almeida. Sou um profissional em transição de carreira, com experiência consolidada como QA e programador back end. Estou animado em compartilhar minha jornada e explorar novas oportunidades no vasto mundo da programação.

- 🧪 Mais de 1 ano de experiência como QA
- 💻 Mais de 3 anos de experiência como programador back end
- 🌱 Em transição de Java para Python

---

## Link

- [LinkedIn](https://www.linkedin.com/in/alexsandro-j-a-almeida/)

---

## Projetos

### Projeto: Calculadora de Despesas

Uma calculadora simples para ajudar a controlar suas despesas diárias. Este projeto é uma ótima maneira de começar a praticar Python e familiarizar-se com seus conceitos básicos.

#### Funcionalidades

- Adicionar despesas
- Visualizar despesas totais
- Calcular média de despesas
- Excluir despesas

#### Exemplo de Uso

```python
class Despesa:
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor

class CalculadoraDespesas:
    def __init__(self):
        self.despesas = []

    def adicionar_despesa(self, descricao, valor):
        self.despesas.append(Despesa(descricao, valor))

    def calcular_total(self):
        return sum(despesa.valor for despesa in self.despesas)

    def calcular_media(self):
        total = self.calcular_total()
        return total / len(self.despesas)

    def excluir_despesa(self, descricao):
        self.despesas = [despesa for despesa in self.despesas if despesa.descricao != descricao]

Contribuições
Contribuições e feedbacks são bem-vindos! Sinta-se à vontade para entrar em contato comigo através do meu LinkedIn para discutir ideias, colaborações ou apenas para dizer olá.

```
