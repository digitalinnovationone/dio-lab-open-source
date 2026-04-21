menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        deposito = float(input("Digite o valor do depósito: "))
        saldo += deposito
        extrato.append(f"DEPOSITO: + R${deposito:.2f}.")
        print(f"Saldo atual da conta: {saldo}")

    elif opcao == "s":
        print("Saque")

        if numero_saques < LIMITE_SAQUES:
            if saldo >= limite:
                valor_saque = float(input("Digite o valor de saque que deseja: "))
            
                if valor_saque > limite:
                    print("O valor desejado excede o limite, tente outro valor.")
                else:
                    numero_saques += 1 
                    extrato.append(f"SAQUE: -R${valor_saque:.2f} {numero_saques}/{LIMITE_SAQUES}.")
                    print("Saque realizado, retire o dinheiro")
            else:
                print("Não será possível sacar o dinheiro por falta de saldo")

        else: 
            print("Você não pode fazer mais saques hoje.")

    elif opcao == "e":
        print("Extrato")

        if extrato:
            print("\n ========== EXTRATO =========")
            print('\n'.join(extrato))
            print("\n ============================")
            print(f"Saldo atual da conta: {saldo}")
        else:
            print("Não foram realizadas movimentações.")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor, selecione novamente a operação desejada.")
