menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

      opção = input(menu)

      if opção =="1":
            valor = float(input("informe o valor de deposito: "))

            if valor >0:
                  saldo += valor
                  extrato += f"Deposito: R$ {valor:.2f}\n"

            else:
                  print("Operação falhou! O valor informado é invalido.")

      elif opção == "2":
           valor = float(input("informe o valor do saque: "))

           excede_saldo = valor > saldo
           
           excedeu_limite = valor > limite

           excedeu_saques = numero_saques >= LIMITE_SAQUES

           if excede_saldo:
                 print("Operação falhou! voce não tem saldo suficiente.")

           elif excedeu_limite:
                 print("operação falhou! o valor do saque excede o limite.")

           elif excedeu_saques:
                 print("operação falhou! Numero maximo de saques excedido.")

           elif valor > 0:
                 saldo -= valor
                 extrato += f"Saque: R$ {valor:.2f}\n"
                 numero_saques += 1
                 
           else:
                 print("operação falhou! o valor informado é invalido.")
            
      elif opção =="3":
        
           print("\n==========EXTRATO==========.")
           print("nao foram realizadas movimentaçoes." if not extrato else extrato)
           print(f"\nsaldo: R$ {saldo:.2f}")
           print("==============================")
           
      elif opção =="4":
           
           break
      else:
            print("operação invalida, por favlor selecione novamente a operação desejada.")
