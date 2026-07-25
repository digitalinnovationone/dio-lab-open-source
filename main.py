from datetime import date
data = date.today().strftime('%d/%m/%Y')


menu = """
[d] - Depositar
[s] - Sacar
[e] - Extrato
[x] - sair
=> """ 

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3 

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("informe o valor a depositar: "))
        
        if valor > 0:
           saldo += valor
           extrato += f"\n Deposito: {valor:.2f} - {data} \n "
        else:
            print ("Operaçao falhou, O valor informado é invalido!")    
    
    elif opcao == "s":
         valor = float(input("informe o valor do saque: "))
        
         execedeu_saldo = valor > saldo
         
         execedeu_limite = valor > limite

         excedeu_saque = numero_saques >= LIMITE_SAQUES
         
         if execedeu_saldo:
             print("Operação falhou, sem saldo suficiente")

         elif execedeu_limite:
             print("Operção falhou, Voce pode sacar ate 500,00 por dia!")
         
         elif excedeu_saque:
             print("Operação falhou,Limite diário de saque excedido")
        
         elif valor > 0:             
             saldo -= valor
             extrato += f"Saque: {valor:.2f} - {data} \n "
             numero_saques+=1  
         else:
             print("Operação falhou, valor informado invalido!")
    
    elif opcao == "e":
        print(f"\n ############## EXTRATO ##############")
        print(f"\n Nao houve movimentacao."if not extrato else extrato)
        print(f"\n Saldo:Rs {saldo:.2f}")
        print(f"\n #####################################")
    
    elif opcao == "q":
        break
    
    else:
        print("Escolha uma operação valida")

