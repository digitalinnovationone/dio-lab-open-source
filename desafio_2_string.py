menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Entre com o valor a ser depositado:"))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n" 
        else:
            print("Valores devem ser positivos")
            
        

    elif opcao == "s":
        saque = float(input("Entre com o valor que gostaria de sacar:"))
        if saque > saldo:
            print("Saldo menor que o valor desejado")
        elif saque > 500:
            print("Valor desejado deve ser menor que R$ 500,00")
        elif numero_saques < LIMITE_SAQUES:
            saldo -= saque
            extrato += f"Saque: -R$ {saque:.2f}\n"
            numero_saques += 1
            print("Saque efetuado")
        else:
            print("Quantidade maxima de saques diarios efetuada")
        
    
    elif opcao == "e":
        print("Extrato".center(15,"#"))
        print(f"Saldo: {extrato}\n")
        print(f"Saldo: {saldo:.2f}\n")
        print("FIM".center(15, "#"))
        

    elif opcao == "q":
        break

    else:
        print("Opçao Inválida")
        
   
