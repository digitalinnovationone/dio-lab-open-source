import time
# Menu Principal a ser exibido

menu = '''
Selecione uma opção:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
'''

# Variáveis que serão necessários para inicío do sistema bancário
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
numero_movimentacao = 0
LIMITE_SAQUES = 3

# O script do sistema bancário
while True:
    opcao = input(menu)

    # Script para DEPÓSITO
    if opcao.lower() == 'd':
        valor_deposito = float(input('Qual o valor do seu depósito? R$'))
        if valor_deposito > 0:
            saldo = saldo + valor_deposito
            numero_movimentacao = numero_movimentacao + 1
            extrato = extrato + f'Movimentação #{numero_movimentacao:.0f} ==> Depósito no valor de +R${valor_deposito:.2f}\n'
            print('O depósito está sendo processado [...]')
            time.sleep(1)
            print('[...]')
            time.sleep(1)
            print('[...]')
            time.sleep(1)
            print(f'Deposito no valor de R${valor_deposito:.2f} realizado com sucesso!')
        else:
            print('O valor a ser depositado deve ser maior que R$0,00')

    # Script para SAQUE
    elif opcao.lower() == 's':
        print('Seu limite de saque é de R$500,00')
        valor_saque = float(input('Qual o valor do seu saque? R$'))
        if valor_saque > saldo:
            print('Saldo atual é insuficiente!')
        elif valor_saque <= 0:
            print('O valor do saque deve ser maior que R$0,00')
        elif valor_saque <= saldo and valor_saque <= 500 and numero_saques < LIMITE_SAQUES:
            numero_saques = numero_saques + 1
            saldo = saldo - valor_saque
            numero_movimentacao = numero_movimentacao + 1
            extrato = extrato + f'Movimentação #{numero_movimentacao:.0f} ==> Saque no valor de -R${valor_saque:.2f}\n'
            print('Seu saque está sendo processado [...]')
            time.sleep(1)
            print('[...]')
            time.sleep(1)
            print('[...]')
            time.sleep(1)
            print(f'Saque no valor de R${valor_saque:.2f} realizado com sucesso!')
        elif valor_saque <= saldo and valor_saque <= 500 and numero_saques >= LIMITE_SAQUES:
            print('Limite de saques diários excedidos!')
        elif valor_saque <= saldo and valor_saque > 500:
            print('Este valor excede o limite de saque para sua conta!')
        else:
            print('Valor informado para saque é inválido!')

    # Script para EXTRATO
    elif opcao.lower() == 'e':
        print(f'Seu saldo atual é de R${saldo:.2f} \nSegue abaixo extrato da sua conta bancária:\n', extrato)

    # Script para SAIR
    elif opcao.lower() == 'q':
        print('Você saiu do sistema COM SEGURANÇA!')
        break
    else:
        print('OPÇÃO INVÁLIDA, selecione novamente a opção desejada!')