# Desafio v2 - Sistema Bancário com Funções Python

'''
Separar as funções existentes de saque,
depósito e extrato em funções. Criar
duas novas funções: cadastrar usuário (cliente) e
cadastrar conta bancária.

# Saque
- A função saque deve receber os 
argumentos apenas por nome (keyword only).

- Sugestão de argumentos: saldo, valor, extrato,
limite, numero_saques, limite_saques. 

- Sugestão de retorno: saldo e extrato

# Depósito
- A função depósito deve receber os
argumentos apenas por posição (positional only).

- Sugestão de argumentos: saldo, valor, extrato.

- Sugestão de retorno: saldo e extrato.

# Criar usuário (cliente)
- O programa deve armazenar os usuários
em uma lista, um usuário é composto por:
nome, data de nascimento, cpf e endereco.
O endereço é uma string com o formato:
logradouro, numero - bairro - cidade/sigla estado.
Deve ser armazenado somente os números do CPF.
Não podemos cadastar 2 usuários com o mesmo CPF.

# Criar conta corrente

- O programa deve armazenar contas em uma lista,
uma conta é composta por: agência, numero da conta e usuário.
O número da conta é sequencial, iniciando em 1.
O número da agência é fixo: "0001". O usuário pode ter
mais de uma conta, mas uma conta pertence a somente um 
usuário.

* Para vincular um usuario a uma conta,
filtre a lista de usuários buscando o 
número do CPF informado para cada usuário
da lista.
'''  
import textwrap

def menu():
    menu = """\n
  ------------------- MENU --------------------
  [d]\tDepositar
  [s]\tSacar
  [e]\tExtrato
  [nc]\tNova conta
  [lc]\tListar contas
  [nu]\tNovo usuário
  [q]\tSair
  ==> """ 
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: \tR$ {valor:.2f}\n"
        print("\n Depósito realizado com sucesso!")
    else:
        print("\n Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    execedeu_saldo = valor > saldo
    execedeu_limite = valor > limite
    execedeu_saques = valor > limite_saques

    if execedeu_saldo:
        print("\n Operação falhou!. Saldo Insuficiente")

    elif execedeu_limite:
        print("\n Operação falhou! O valor do saque execede o limite")
    
    elif execedeu_saques:
        print("\n Operação falhou! Número máximo de saques execedido")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n Saque realizado com sucesso!")

    else:
        print("\n Saque realizada com sucesso!")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n--------------- EXTRATO -----------------------")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números):")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n CPF já cadastrado!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa):")
    endereco = input("Informe o endereço (logradouro, numero - bairro - cidade/sigla estado):")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")
        
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n Usuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,

            )
        elif opcao == "e":
            exibir_extrato(saldo, extrato = extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()

        
