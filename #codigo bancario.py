#codigo_bancario
saldo = 1500

def menu(): #string tripla para criar o menu
    print("""                           
    =========================
          MENU PRINCIPAL
    =========================
    1 - Depositar
    2 - Sacar
    3 - Exibir saldo
    4 - novo cliente
    5 - Extrato
    6 - Sair
    =========================
    """)

menu()
opcao = input("Escolha uma opção: ")

if opcao == "1":
    deposito = float(input("deposito selecionado, insira o valor desejado: "))
    if deposito <= 0:  # para exibir a mensagem apenas quando for menor ou igual a 0
        print("operação incorreta, tente novamente")
    elif deposito > 0:
         saldo += deposito
    print(f"Depósito concluído com sucesso! Saldo atual: R$ {saldo:.2f}")            

elif opcao == '2':
    saque = float(input("opção de saque selecionada, insira o valor desejado: "))
    if saque < saldo: 
        saldo -= saque
        print(f"Saque realizado com sucesso! Seu saldo é de R$ {saldo:.2f}")
    elif saque > saldo:
            print("Valor insuficiente!")
            
elif opcao == '3':
    print(f"Seu saldo atual é de R$ {saldo:.2f}")

elif opcao == '4':

    idade = int(input("Sua idade: "))

    if idade >= 18:
        print("insira seus dados para abertura da conta") 
        cpf = input("CPF: ")
        rg = input("RG: ") 
        renda = float(input("Renda mensal:  "))
        print("Conta aprovada, entre 1 a 2 horas sua conta estará disponivel para utilização,\n Agradecemos a preferencia!!!")
    else:
        print("A idade mínima para abrir a conta é 18 anos. Agradecemos a preferência!")

elif opcao == '5':
    print(f"""                           
    =========================
    NENHUMA OPERAÇÃO REALIZADA
    SEU SALDO É DE R$ {saldo:.2f}
    ==========================""")

 
elif opcao == '6':
    print('obrigado pela preferencia, até a proxima!')

else: 
    print("Opção invalida, tente novamente!")



