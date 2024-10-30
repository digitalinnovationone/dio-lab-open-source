# lista para armazenar cliente ( utilizamos lista porque permite armazenar multiplos registros. Cada cliente será um item dessa lista Cliente)
clientes = []
contas = []

# função para adicionar cliente 
def adiciona_cliente():
    nome = input("Digite o nome para cadastro do cliente: ")
    data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
    cpf = input("Digite o cpf (apenas os números): ").replace(".", "").replace("-", "")
    endereco = input("Digite o endereço (logradrouro, numero - bairro - cidade/sigla_estado): ")

    # verificar se cliente já existe
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            print("Erro: CPF já cadastrado")
            return
    
    # Criando um dicionario para o cliente
    novo_cliente = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    # adicionar cliente em uma lista
    clientes.append(novo_cliente) # o metodo append() adiciona o novo cliente à lista de clientes
    print("Cliente adicionado com sucesso!")

# Função para criar conta corrente
def criar_conta_corrente():
    cpf = input("Digite o CPF do cliente para criar a conta corrente: ")
    #verificar se o cliente existe
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            cliente_ja_existe = cliente
            break
    if cliente_ja_existe is None:
        print("Cliente não contém cadastro.")
        return
    numero_conta = len(contas)+1
    nova_conta = {
        'numero_conta': numero_conta,
        'cliente': cliente_ja_existe,
        'saldo': 0.0,
        'historico': []
    }
    contas.append(nova_conta)
    print(f"Conta criada com sucesso! Número da conta é: {numero_conta}")

# Definindo as funções (depositar, sacar, extrato nova conta)
# função depositar

def depositar():
    numero_conta = int(input("Digite o numero da conta corrente: "))
    valor = float(input("Digite o valor do depósito: "))

    # validar se conta existe
    for conta in contas:
        if conta['numero_conta'] == numero_conta:
            conta['saldo'] += valor
            conta['historico'].append(f"Depósito de R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        return
    print("Conta não existe.")

# função para sacar
def sacar():
    numero_conta = int(input("Digite o numero da conta corrente: "))
    valor = float(input("Digite o valor do saque: "))

    # validar conta corrente
    for conta in contas:
        if conta['numero_conta'] == numero_conta:
            if conta ['saldo'] >= valor:
                conta['saldo'] += valor
                conta['historico'].append(f"Saque de R${valor:.2f}")
                print(f"Saque de R${valor:.2f} realizado com sucesso!")
            else:
                print("Saldo insuficiente.")
            return
    print("Conta não existe.")

# função para visualizar as transações
def extrato():
    numero_conta = int(input("Digite o número da conta corrente: "))

    # encontrar a conta corrente
    for conta in contas:
        if conta['numero_conta'] == numero_conta:
            print(f"Extrato da conta {numero_conta}: ")
            for transacao in conta['historico']:
                print(transacao)
            return 
    print("Conta não encontrada.")

# menu de opções para conta
while True:
    print("\n*************Banco Digital*************")
    print("1. Cadastrar cliente")
    print("2. Cadastrar Conta Corrente")
    print("3. Depositar")
    print("4. Sacar")
    print("5. Extrato")
    print("6. Sair")
    print("\n***************************************")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adiciona_cliente()
    elif opcao == "2":
        criar_conta_corrente()
    elif opcao == "3":
        depositar()
    elif opcao == "4":
        sacar()
    elif opcao == "5":
        extrato()
    elif opcao =="6":
        break
    else:
        print("Opção inválida")