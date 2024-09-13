menu = """
[D]-> depositar 
[S]-> sacar 
[E]-> extrato 
[Q]-> sair 
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d" or opcao == "D":
        valor = float(input("Valor a ser depositado: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou, valorinformado é invalido")
    
    elif opcao == "s" or opcao == "S":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Saldo insuficiente!!")
        
        elif excedeu_limite:
            print("Limite insuficiente!!")
        
        elif excedeu_saque:
            print("Numero maximo de saques excedido!!")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
        else:
            print("Valor informado invalido...")
    
    elif opcao == "e" or opcao == "E":
        print("\n============================= EXTRATO =================================")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print (f"\nSaldo R$ {saldo:.f2}")
        print("=========================================================================")
    
    elif opcao == "q" or opcao == "Q":
        break
    
    else:
        print("Opção invalida, selecione a opção desejada novamente")