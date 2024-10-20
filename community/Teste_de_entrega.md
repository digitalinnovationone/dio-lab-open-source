
# Primeira entrega do projeto

Nesse 1° entrega, apreveitei o codigo do professor e fiz algumas adaptações na sua estrutura.
Estou gostando muito do curso.

## 📚 Site
-[Site da Dio](https://www.dio.me/)

Testando minha entrega!!

## Código:
    Menu = """
    Olá, digite uma das opções Informadas:
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

    opcao = input(menu)

    if opcao == "1":
        print("\n================ DEPOSITO ================")
        valor = float(input("Atenção: Limite de saque é de R$500 reais por operação e limite de saque de no máximo 3 vezes por dia!\n\nInforme o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        print("\n================ SAQUE ================")
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! Limite maximo de saque por operação é de no maximo R$500 reais. tente novamente!")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques diário excedido. Por questões de segurança, tente novamente amanhã! Obrigado.")
            break

        elif valor > 0:
            saldo -= valor
            extrato += f"Valor do saque: R$ {valor:.2f}\n"
            print(f"\nSeu novo saldo agora é: R$ {saldo:.2f}")
            numero_saques += 1
                
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Informação do saldo atual da sua conta!" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
    print("Volte sempre!!")
=========== Obrigado!! ============
