menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=>"""


saldo = 0
limite = 500
extrato = ""
numero_saques= 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == 1:
        valor = float(input('Informe o valor do dep�sito: '))
        
        if valor > 0:
            saldo += valor
            extrato += f"Dep�sito: R${valor:.2f}\n"
        else:
            print('Opera��o falhou! Valor informado inv�lido.')
            
    
    elif opcao == 2:
        valor = float(input('Informe o valor do saque: '))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print('Opera��o falhou! Voc� n�o tem saldo suficiente.')
        
        elif excedeu_limite:
            print('Opera��o falhou! Valor de saque excede o limite.')
        
        elif excedeu_saques:
            print('Opera��o falhou!N�mero m�ximo de saques excedido.')
        
        elif valor >0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
    
    elif opcao == 3:
        print("\n===============EXTRATO===============")
        print("N�o foram realizadas movimenta��es." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print('=======================================')
    
    elif opcao == 4:
        print('Sair')
    
    else:
        print('Opera��o inv�lida, por favor seleciona novamente a opera��o desejada!')
        
    