print("\n================ Menu Principal ================")

menu = """
[0] Sair
[1] Depositar
[2] Sacar
[3] Extrato
[4] Abrir conta pj
[5] Consultar conta pj 
 

Escolha uma opção de 0-5
=> """


consultar_conta = 0
saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor para depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else: 
            print("Operação Falhou. O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedido_saldo = valor > saldo
        excedido_limite = valor > limite
        excedido_saque = numeros_saques >= LIMITE_SAQUES

        if excedido_saldo:
            print("Operação falhou. Saldo insuficiente.")

        elif excedido_limite:
            print("Operação falhou. Valor de saque excede o limite.")

        elif excedido_saque:
            print("Operação falhou. Limite de saques excedidos.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numeros_saques += 1

        else:
            print("Operação falhou. Valor informado é inválido.")


    elif opcao == "3":
        print("\n------------------------ EXTRATO ------------------------")
        print("Não foram realizadas transações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("-----------------------------------------------------------")

    elif opcao == "0":
        print("============================================")
        print("==  Obrigado por utilizar nossos sistemas ==")
        print("============================================")
        break
    
    elif opcao >= "6":
        print("Operação inválida, por favor selecione uma operação desejada.")    

    
    if opcao == "4":
        valor = float(input("Informe o CNPJ da empresa: "))
        nome = str(input("Informe seu nome: "))
        
        print("\nCNPJ cadastrado:  ", valor)
        print("Nome cadastrado:", nome)
        print(f"\nTitular da conta é {nome} e o CNPJ cadastrado é {valor}")
        print("\nConta cadastrada com sucesso.")



    elif opcao == "5":
        print("\n----------------- CONSULTAR CONTA PJ CADASTRADA -----------------")
        print("Não foram realizadas movimentações" if not consultar_conta else consultar_conta)
        print(f"\nNome cadastrado: {nome}")
        print(f"\nCnpj cadastrado: {valor}")
        print("-------------------------------------------------------------------")    










  
            