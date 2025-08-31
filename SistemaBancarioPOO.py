from abc import ABC, abstractmethod
from datetime import datetime

# ---------------- CLASSES DE TRANSAÇÕES ----------------
class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if self.valor > 0:
            conta._saldo += self.valor
            conta.historico.adicionar_transacao(self)
            print(f"=== Depósito de R$ {self.valor:.2f} realizado com sucesso! ===")
        else:
            print("@@@ Operação falhou! Valor inválido. @@@")


class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if self.valor <= 0:
            print("@@@ Operação falhou! Valor inválido. @@@")
        elif self.valor > conta._saldo:
            print("@@@ Operação falhou! Saldo insuficiente. @@@")
        elif isinstance(conta, ContaCorrente) and conta.numero_saques >= conta.limite_saques:
            print("@@@ Operação falhou! Limite de saques excedido. @@@")
        elif isinstance(conta, ContaCorrente) and self.valor > conta.limite:
            print("@@@ Operação falhou! Valor acima do limite. @@@")
        else:
            conta._saldo -= self.valor
            conta.numero_saques += 1
            conta.historico.adicionar_transacao(self)
            print(f"=== Saque de R$ {self.valor:.2f} realizado com sucesso! ===")


# ---------------- CLASSES DE APOIO ----------------
class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })

    def mostrar(self, saldo):
        print("\n===== EXTRATO =====")
        if not self.transacoes:
            print("Não foram realizadas movimentações.")
        else:
            for t in self.transacoes:
                print(f"{t['data']} - {t['tipo']}: R$ {t['valor']:.2f}")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================")


# ---------------- CLASSES DE CONTA ----------------
class Conta:
    def __init__(self, numero, cliente, agencia="0001"):
        self._saldo = 0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    def sacar(self, valor):
        return Saque(valor).registrar(self)

    def depositar(self, valor):
        return Deposito(valor).registrar(self)


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saques = 0


# ---------------- CLASSES DE CLIENTE ----------------
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento


# ---------------- MAIN ----------------
def main():
    clientes = []
    contas = []

    # Criar cliente
    cliente = PessoaFisica(nome="Gustavo Ramos", cpf="12345678900", data_nascimento="01-01-2000", endereco="Rua A, 123")
    clientes.append(cliente)

    # Criar conta
    conta = ContaCorrente(numero=1, cliente=cliente)
    cliente.adicionar_conta(conta)
    contas.append(conta)

    # Testando operações
    cliente.realizar_transacao(conta, Deposito(1000))
    cliente.realizar_transacao(conta, Saque(200))
    cliente.realizar_transacao(conta, Saque(100))

    conta.historico.mostrar(conta.saldo)


if __name__ == "__main__":
    main()
