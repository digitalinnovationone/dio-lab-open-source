'''
Sistema Bancário
- Operações: sacar, depositar e visualizar 
o extrato

Operação de deposito
- Deve ser possivel depositar valores
positivos para a conta bancaria. Todos os 
depósitos devem ser armazenados em 
uma variavel e exibidos na operação
de extrato.

Operação de saque
- O sistema deve permitir realizar 3 saques diarios no limite maximo de RS 500,00 por saque.
Caso o usuário não tenha saldp em conta, o sistema deve exibir uma mensagem informandp que não será possível sacar o
dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variavel e exibidos na operação de 
extrato.

Operação de extrato
- Essa operação deve listar todos os depositos e saques realizados na
conta. No fim da listagem deve ser exibido o saldo atual da conta.

Os valores devem ser exibidos utilizando o formato RS xxx.xx.

'''


menu = """


[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """ 

saldo = 0
limite = 500
extrato = " "
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if (valor>0):
            saldo += valor
            extrato +=f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou: O valor informado é inválido.")


    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        execedeu_saldo = valor > saldo

        execedeu_limite = valor > limite

        execedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if execedeu_saldo:
            print("Operação falhou! Saldo insulficiente")
        
        elif execedeu_limite:
            print("Operação falhou. O valor do saque excede o limite de 500 reais.")

        elif execedeu_saques:
            print("Operação falhou! Numero maximo de saques execedido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido")


    elif opcao == "e":
       print("\n***************** EXTRATO ******************")
       print("Não foram realizadas movimentações." if not extrato else extrato)
       print(f"\nSaldo: R$ {saldo:.2f}")
       print("**********************************************")


    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

    