# Para a primeira versão do sistema devemos implementar apenas 3 operações:
# depósito, saque e extrato

# 1. Deve ser possível depositar valores positivos para a minha conta bancária
# 2. A V.1 trabalha apenas com 1 usuário, dessa maneira não precisamos identificar qual é o numero da agência e conta bancária.
# 3. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato
# 4. O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque.
# 5. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando quer não será possível sacar o dinheiro por falta de saldo
# 6. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extato


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
limite_saques = 3
valor_minimo = 20

while True:
    opcao = input(menu)
    # se a opcao for igual deposito 
    if opcao == "d":
        # apresente a opção selecionada
        print("Deposito")
        valor = float(input("Informe o valor do deposito: "))
        # valida se valor é maior que 0
        if valor > 0:
            # se Sim então soma esse valor no saldo
            saldo += valor
            # adiciona valor adicionado ao extrato para apresentar na tela quando solicitado
            extrato += f"Deposito R$ {valor:.2f}\n"
        else:
            # senão exibe mensagem de falha para o usuário
            (f"Operação falhou! O valor informado é invalido.")
    # se a opção for igual a saque
    elif opcao == "s":
        # apresente a opção selecionada
        print("Saque")
        # variável valor recebe o valor do saque
        valor = float(input("Informe o valor do saque: "))
        # armazenando valor nas variaveis declaradas 
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques
        valor_minimo = valor < 20
        # se valor informado for maior do que o saldo da conta informar saldo insuficiente
        if excedeu_saldo:
            print("\nOperação falhou! Saldo insuficiente.")
        # se valor do saque for maior do que o valor contido na variável saldo informar limite excedido
        elif excedeu_limite:
            print("\nOperação falhou! O valor do saque excede o limite")
        # se valor do saque for maior do que o permitido para o dia  informar que o valor excede o limite do dia
        elif excedeu_saques:
            print("\nOperação falhou! Número máximo de saques excedido.")
        elif valor_minimo:
            print("\nValor mínimo para saques é de R$ 20.00.")
        # se valor for maior que zero
        elif valor > 20:
            # subtraia do saldo o valor informado no limite de até 500
            saldo -= valor
            # acrescenta na variavel extrato mais uma operação executada
            extrato += f"Saque: R$ - {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")
    # opção extrato apresenta na tela as variáveis chamadas anteriormente
    elif opcao == "e": 
        print("\n===============Extrato===============")
        print("Não foram ralizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n=======================================")
    # essa opção para a execução do programa
    elif opcao == "q":
        break

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada")
