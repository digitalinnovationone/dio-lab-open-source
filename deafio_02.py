import time
from decimal import Decimal

decimal_precision = Decimal('0.01')     # Definir precisão decimal

def menu():     # Função exibir menu

    menu = f"""
    Seja bem vindo(a)!

    [1] Depositar
    [2] Sacar
    [3] Extrato
    
    [4] Nova conta
    [5] Listar contas
    [6] Novo usuário
    
    [0] Sair


    Digite a opção desejada e telcle [Enter]
    => """
    return input(menu)
    
def depositar(valor_deposito, saldo, extrato):
        
    if valor_deposito > 0:
            
        saldo += valor_deposito
        extrato += f"{time.strftime('%d/%m/%y %X')}  |    Depósito   |  R$ {valor_deposito:.2f}\n"

        print(f"Depósito realizado com sucesso!")
        return extrato, saldo # Registrando saldo e extrato atualizados
        
    else:
        print("Operação falhou! O valor informado é inválido.")
        return extrato, saldo # Mantendo valores anteriores
        
def sacar (valor_saque, limite, quantidade_saques, LIMITE_SAQUES, saldo, extrato):
    if 0 < valor_saque <= saldo and valor_saque <= limite and quantidade_saques < LIMITE_SAQUES:
            
        saldo -= valor_saque
            
        extrato += f"{time.strftime('%d/%m/%y %X')}  |    Saque      | (R$ {valor_saque:.2f})\n"
            
        quantidade_saques += 1
                
        print("Saque ralizado com sucesso!")
        return extrato, saldo, quantidade_saques
       
    else:
        print("Operação falhou! Verifique seu limite de saque ou quantidade de saques.")
        return extrato, saldo, quantidade_saques

def filtrar_usuario(cpf, usuarios):     # Função filtar usuário pelo CPF
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):        # Função criar novo usuário
    cpf = input("\nInforme o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:     # Verificar se usuário já existe
        print("\nCPF vinculado a um usuário existente.")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("Usuário criado com sucesso!")     
        

def criar_conta(agencia, numero_conta, usuarios):       # Função criar nova conta
    
    cpf = input("Informe o CPF(somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario: 
        conta_cc = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        print(f"\nConta: {numero_conta} \nAgencia: {agencia} \nConta criada com sucesso!!!") 
        return conta_cc
        
    else:
        print("Usuário não encontrado. Use um CPF cadastrado.")     
        return None

def acesso_menu():      # Função acessar menu
    
    decimal_precision = Decimal('0.01')
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = Decimal('0')
    limite = Decimal('500')
    extrato = ""
    quantidade_saques = 0
    usuarios = []
    contas = []
    

    while True:
    
        opcao = menu()

        if opcao == "1":        # Depositar
            valor_deposito = Decimal(input("Informe o valor do depósito: R$ "))
            
            extrato, saldo = depositar(valor_deposito, saldo, extrato)


        elif opcao == "2":      # Sacar
            com_saldo = saldo > 0

            if not com_saldo:
                print("Saque não disponível. Verifique seu saldo.")

            else :
            
                valor_saque = Decimal(input("Informe o valor do saque: R$ "))
                extrato, saldo, quantidade_saques = sacar (valor_saque, limite, quantidade_saques, LIMITE_SAQUES, saldo, extrato)


            
        elif opcao == "3":      # Exibir extrato
            
            data_hora = time.localtime()
            data = time.strftime('%d/%m/%y',data_hora)
            hora = time.strftime('%H:%M:%S',data_hora)

            extrato_formatado = f"Não há registro de movimentações.\n" if not extrato else extrato
        
            saldo_formatado = f"\nSaldo em {data} {hora}:           R$ {saldo:.2f}"

            print("\n===================== EXTRATO =====================")
            print("\n===================================================")
            print("Data/Hora          |   Operação    |    Valor")
            print("===================================================")
            print(extrato_formatado)
            print(saldo_formatado)
            print("======================= FIM =======================")

        elif opcao == "4":      # Nova conta
            agencia = AGENCIA
            numero_conta = len(contas) + 1
            conta_cc = criar_conta(agencia, numero_conta, usuarios)
            
            if conta_cc:
                contas.append(conta_cc)
                
        elif opcao == "5":  # Listar contas
            if contas:
                print("\nContas cadastradas:")
                for conta_cc in contas:
                    linha = f"""
                    Agência: {conta_cc['agencia']}
                    C/C: {conta_cc['numero_conta']}
                    Titular: {conta_cc['usuario']['nome']}
                    """
                    print("=" * 100)
                    print(linha)
            else:
                print("\nNão há contas cadastradas.")
                

        elif opcao == "6":      # Novo usuário
            criar_usuario(usuarios)
                    
        elif opcao == "0":      # Sair
            print(f"Obrigado por usar nossos Serviços!")
            break

        else:       # opção inválida
            print("Operação inválida, por favor selecione uma opção disponível.")
            
acesso_menu()