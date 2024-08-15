# Minha primeira contribuição!!! 😊🚀

Essa é minha primeira contribuição, vou guardar esse readme por bastante tempo pra quando eu for um DEV excelente, vou olhar esse readme e me lembrar de todo o meu esforço pra chegar onde cheguei, agora é foco nos estudos! (SEMPRE KKKKKKKK)

Linguagem que estou me especializando:

![Python](https://img.shields.io/badge/Python-000?style=for-the-badge&logo=python)

Conecte-se comigo!

[![LinkedIn](https://img.shields.io/badge/LinkedIn-000?style=for-the-badge&logo=linkedin&logoColor=0E76A8)](https://https://www.linkedin.com/in/guilherme-felix-pascoal-587790204//)

[![Instagram](https://img.shields.io/badge/Instagram-000?style=for-the-badge&logo=instagram)](https://www.instagram.com/felix__gui/)

Vou deixar uma calculadora com while que eu fiz em Python:

""" Calculadora com while """
while True:

    num1 = input ('Digite um número: ')
    num2 = input ('Digite outro número: ')
    operador = input ('Digite o operador +|-|/|*: ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(num1)
        num_2_float = float(num2)
        numeros_validos =  True

    except:
        numeros_validos = None


    if numeros_validos is None:
        print('Um ou ambos os números digitados são invalidos.')
        continue
    

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido!')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador!')
        continue

    print('Realizando sua conta. Confira o resultado abaixo:')

    if operador == '+':

        print(f'{num_1_float} + {num_2_float} = ', num_1_float + num_2_float)

    elif operador == '-':

        print(f'{num_1_float} - {num_2_float} = ', num_1_float - num_2_float)

    elif operador == '/':

        print(f'{num_1_float} / {num_2_float} = ', num_1_float / num_2_float)

    elif operador == '*':

        print(f'{num_1_float} * {num_2_float} = ', num_1_float * num_2_float)

    else:
        print('Nunca deveria chegar aqui.')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
