import random
n1 = str(input('Primeiro jogador: '))
n2 = str(input('Segundo jgoador: '))
n3 = str(input('Terceiro jogador: '))
n4 = str(input('Quarto jogador: '))
n5 = str(input('Quinto Jogador: '))
n6 = str(input('Primeiro jogador: '))
n7 = str(input('Segundo jogador: '))
n8 = str(input('Terceiro jogador: '))
n9 = str(input('Quarto jogador: '))
n10 = str(input('Quinto Jogador: '))
lista= [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]
random.shuffle(lista)
timea = lista[:5]
timeb = lista[5:]
print(f'O time A vai ser{timea} e o time B vai ser {timeb}')


