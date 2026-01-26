from datetime import datetime

# ==============================
# CLASSE TRANSACAO
# ==============================
class Transacao:
    def __init__(self, tipo, valor):
        self.tipo = tipo  # 'Depósito' ou 'Saque'
        self.valor = valor
        self.data = datetime.now()

    def __str__(self):
        return f"{self.data.strftime('%d/%m/%Y %H:%M:%S')} - {self.tipo}: R$ {self.valor:.2f}"

# ==============================
# CLASSE CLIENTE
# ==============================
class Cliente:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = ''.join(filter(str.isdigit, cpf))
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

# ==============================
# CLASSE CONTA
# ==============================
class Conta:
    contador = 1000

    def __init__(self, cliente):
        self.numero = Conta.contador
        Conta.contador += 1
        self.cliente = cliente
        self.saldo = 0.0
        self.extrato = []  # lista de Transacao
        self.limite = 500.0
        self.numero_saques = 0
        self.limite_saques = 3
        cliente.adicionar_conta(self)

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido para depósito.")
            return
        self.saldo += valor
        self.extrato.append(Transacao("Depósito", valor))

    def sacar(self, valor):
        if self.numero_saques >= self.limite_saques:
            print("Limite de saques atingido.")
            return
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return
        if valor > self.limite:
            print("Valor excede o limite por saque.")
            return
        self.saldo -= valor
        self.extrato.append(Transacao("Saque", valor))
        self.numero_saques += 1

    def mostrar_extrato(self):
        print(f"\nExtrato da conta {self.numero} - Cliente: {self.cliente.nome}")
        if not self.extrato:
            print("Nenhuma movimentação registrada.")
        else:
            for movimento in self.extrato:
                print(movimento)
        print(f"Saldo atual: R$ {self.saldo:.2f}")

# ==============================
# CLASSE BANCO
# ==============================
class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def cadastrar_cliente(self, nome, data_nascimento, cpf, endereco):
        if self.buscar_cliente(cpf):
            print("Cliente já cadastrado!")
            return None
        cliente = Cliente(nome, data_nascimento, cpf, endereco)
        self.clientes.append(cliente)
        return cliente

    def criar_conta(self, cliente):
        conta = Conta(cliente)
        self.contas.append(conta)
        return conta

    def buscar_cliente(self, cpf):
        cpf = ''.join(filter(str.isdigit, cpf))
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def listar_clientes(self):
        for cliente in self.clientes:
            print(f"{cliente.nome} - CPF: {cliente.cpf}")

# ==============================
# MENU INTERATIVO
# ==============================
def menu():
    banco = Banco()

    while True:
        print("\n===== SISTEMA BANCÁRIO =====")
        print("[1] Cadastrar cliente")
        print("[2] Criar conta")
        print("[3] Depositar")
        print("[4] Sacar")
        print("[5] Extrato")
        print("[6] Listar clientes")
        print("[0] Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome: ")
            nasc = input("Data de nascimento (dd/mm/aaaa): ")
            cpf = input("CPF: ")
            end = input("Endereço: ")
            banco.cadastrar_cliente(nome, nasc, cpf, end)

        elif opcao == "2":
            cpf = input("CPF do cliente: ")
            cliente = banco.buscar_cliente(cpf)
            if cliente:
                conta = banco.criar_conta(cliente)
                print(f"Conta criada com sucesso! Número: {conta.numero}")
            else:
                print("Cliente não encontrado.")

        elif opcao == "3":
            num = int(input("Número da conta: "))
            valor = float(input("Valor do depósito: "))
            conta = next((c for c in banco.contas if c.numero == num), None)
            if conta:
                conta.depositar(valor)
            else:
                print("Conta não encontrada.")

        elif opcao == "4":
            num = int(input("Número da conta: "))
            valor = float(input("Valor do saque: "))
            conta = next((c for c in banco.contas if c.numero == num), None)
            if conta:
                conta.sacar(valor)
            else:
                print("Conta não encontrada.")

        elif opcao == "5":
            num = int(input("Número da conta: "))
            conta = next((c for c in banco.contas if c.numero == num), None)
            if conta:
                conta.mostrar_extrato()
            else:
                print("Conta não encontrada.")

        elif opcao == "6":
            banco.listar_clientes()

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

# ==============================
# MAIN
# ==============================
if __name__ == "__main__":
    menu()