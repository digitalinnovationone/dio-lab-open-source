def calculadora():
    print("Bem-vindo à Calculadora!")
    print("Escolha uma operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    
    escolha = input("Digite o número da operação desejada: ")
    
    if escolha in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            resultado = num1 + num2
            operacao = "adição"
        elif escolha == '2':
            resultado = num1 - num2
            operacao = "subtração"
        elif escolha == '3':
            resultado = num1 * num2
            operacao = "multiplicação"
        elif escolha == '4':
            if num2 == 0:
                print("Erro: Divisão por zero não é permitida.")
                return
            resultado = num1 / num2
            operacao = "divisão"

        print(f"O resultado da {operacao} é: {resultado}")
    else:
        print("Opção inválida. Tente novamente.")

calculadora()

