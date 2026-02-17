menu = """
==========================================
        SISTEMA BANCÁRIO 
==========================================

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> Escolha uma opção: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("\n=== DEPÓSITO ===")
        valor = float(input("Informe o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\n✅ Depósito realizado com sucesso!")
        else:
            print("\n❌ Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        print("\n=== SAQUE ===")
        valor = float(input("Informe o valor do saque: R$ "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\n❌ Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("\n❌ Operação falhou! O valor do saque excede o limite de R$ 500.00.")

        elif excedeu_saques:
            print("\n❌ Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:    R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"\n✅ Saque de R$ {valor:.2f} realizado com sucesso!")

        else:
            print("\n❌ Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"\nSaldo:    R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print("\nObrigado por usar nosso banco! 👋")
        break

    else:
        print("\n❌ Operação inválida, por favor selecione novamente a operação desejada.")
