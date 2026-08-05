from datetime import datetime

# Esse projeto trata-se de um sistema bancário simples.
# Estou me baseando no template do professor do curso DioSantander, mas farei de forma mais clara e performática.
# A ideia é explorar mais profundamente a linguagem Python.

# Regras:
# 1 - Não pode sacar valor negativo.
# 2 - Não pode sacar mais de 3 vezes por dia (na execução).
# O extrato deve mostrar: depósitos, saques, data e saldo atual.

class bancoDio:
    
    def __init__(self):
        self.valorConta = 0.0
        self.saques = []     # Lista de tuplas (data, valor)
        self.depositos = []  # Lista de tuplas (data, valor)
        self.limiteDiario = 3

    def deposito(self, valor):
        if valor > 0:
            self.valorConta += valor
            data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            self.depositos.append((data, valor))
            print(f"O valor de R${valor:.2f} foi depositado com sucesso.")
        else:
            print("Erro: O valor deve ser positivo e maior que zero.")

    def realizar_saque(self, valor):
        if len(self.saques) >= self.limiteDiario:
            print("Erro: Você já atingiu o limite diário de saques!")
        elif valor <= 0:
            print("Erro: O valor deve ser maior que zero!")
        elif self.valorConta < valor:
            print("Erro: Saldo insuficiente para saque!")
        else:
            self.valorConta -= valor
            data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            self.saques.append((data, valor))
            print(f"Saque de R${valor:.2f} realizado com sucesso!")

    def exibir_extrato(self):
        print("\n------ EXTRATO COMPLETO ------")

        print("\n>> DEPÓSITOS:")
        if self.depositos:
            for i, (data, valor) in enumerate(self.depositos, 1):
                print(f"{i}. Data: {data} | Valor: R${valor:.2f}")
        else:
            print("Nenhum depósito realizado.")

        print("\n>> SAQUES:")
        if self.saques:
            for i, (data, valor) in enumerate(self.saques, 1):
                print(f"{i}. Data: {data} | Valor: R${valor:.2f}")
        else:
            print("Nenhum saque realizado.")

        print(f"\n>> Saldo atual: R${self.valorConta:.2f}")
        print("------------------------------")


# Instância do banco
banco = bancoDio()

# Loop principal de interação com o usuário
while True:
    print("\n------ BancoDio ------")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Extrato")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        try:
            valor = float(input("Digite o valor que deseja depositar: "))
            banco.deposito(valor)
        except ValueError:
            print("Erro: Digite um valor numérico válido.")

    elif opcao == "2":
        try:
            valor = float(input("Digite o valor que deseja sacar: "))
            banco.realizar_saque(valor)
        except ValueError:
            print("Erro: Digite um valor numérico válido.")

    elif opcao == "3":
        banco.exibir_extrato()

    elif opcao == "0":
        print("Obrigado por usar o BancoDio. Até logo!")
        break

    else:
        print("Opção inválida, tente novamente.")
