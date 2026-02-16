from datetime import date

print(
"""
    ============Bem Vindo=============

    [1] Depositar

    [2] Sacar

    [3] Extrato

    [4] Sair
    
    ===================================
""")

saldo = 0
deposito = 0
saque = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Loop para manter o menu ativo até que o usuário escolha sair

controle = True


while controle:
    resp = input("Digite a opção desejada: ")

    if resp == "1":

        deposito = float(input("Digite o valor que deseja depositar: "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito R$ {deposito:.2f}\n"
            print(f"Você depositou R$ {deposito}")
        else:
            print("O valor informado é inválido")

    elif resp == "2":
        if numero_saques <= LIMITE_SAQUES:
            saque = float(input("Digite o valor que deseja sacar: "))
            
            if saque > limite:
                print("Valor do saque excede o limite de R$ 500,00.")
            elif saque > saldo:
                print("Saldo insuficiente para realizar o saque.")
            elif saque > 0:
                saldo -= saque
                extrato += f"Saque: R$ {saque}\n"
                print(f"Você sacou R$ {saque}. Seu novo saldo é R$ {saldo}.")
                numero_saques += 1
            else:
                print("Valor de saque inválido, por favor tente novamente")
        else:
            print("Número máximo de saques atingido.")

    elif resp == "3":

        print(f""" 

============Extrato=============
        
Movimentações realizadass no dia de hoje ({date.today().strftime('%d/%m/%Y')}):
{extrato if extrato else "Nenhuma movimentação realizada hoje."}

Saldo atual:R$ {saldo:.2f}

=================================

""")
    elif resp == "4":
        print("Você escolheu Sair. Obrigado pela preferência!")
        controle = False
    else:
     print("Opção inválida, tente novamente.")
