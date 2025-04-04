menu = """  
[d] Depositar
[s] Sacar
[e] Extrato
[q]  Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
 
 opcao = input(menu)
 
 if opcao == "d":
     valor = float(input("Informe o valor do depósito: "))
     
     if valor > 0:
          saldo += valor
          extrato += f"Depósito: R$ {valor:.2f}\n"
     else:
            print("Valor inválido para depósito!")
 
 elif opcao == "s":
      valor = float(input("Informe o valor do saque: "))
      excedeu_saldo = valor > saldo
      excedeu_limite = valor > limite
      excedeu_saques = numero_saques >= LIMITE_SAQUES
      
      if excedeu_saldo:
            print("Valor inválido! Saldo insuficiente.")
        
      elif excedeu_limite:
            print("Valor inválido! Excedeu o limite.")
        
      elif excedeu_saques:
            print("Valor inválido! Excedeu o número de saques.")
        
      elif valor > 0:
            saldo -= valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            numero_saques += 1
        
      else:
            print("Valor inválido para saque!")
           
 
 elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
 
 elif opcao == "q":
        print("Saindo...")
        break
 
 else:
     print("Opção inválida!")          
