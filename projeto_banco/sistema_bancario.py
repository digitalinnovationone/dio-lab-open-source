
deposito = float(input("Digite o valor a ser depositado ou 0 para sair!!\n"))
saldo=[]
saldo.append(deposito)

while deposito != 0:
    deposito = float(input("Digite o valor a ser depositado!!\n"))
    saldo.append(deposito)
    print(saldo)
    
saldo_em_conta = print("Saldo atual da conta: \n", sum(saldo))


quantidade_saque_diario = 3
sacar = float(input("Digite o valor que deseja sacar!!\n"))
