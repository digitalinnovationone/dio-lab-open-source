def tela(mostrando):
    
    for l in range(3):
        for ll in range(3):
            if mostrando[l][ll] == 0:
                print("_|", end=' ')
            elif mostrando[l][ll] == 1:
                print("X|", end=' ')
            elif mostrando[l][ll] == -1:
                print("O|", end=' ')

        print()
lista = [[0,0,0],[0,0,0],[0,0,0]]

#tela(lista)

vitoria = 0
rodada = 0
jogador = 0

while (vitoria < 3) or (vitoria > -3): # looping
    jogador = rodada % 2 + 1
    print(f"jogador {jogador}." )
    tela(lista) #puxando o que vai aparecer para jogar def dentro de def
    
    linha = int(input("\n Escolha a linha: ")) # se linha coluna maior que os numeros informados pedir de novo.
                
    while (linha < 1 or linha > 3):  
        linha = int(input("\n Escolha a linha: "))
    linha = linha -1 # deixando a variavel linha na posição 0
    
    coluna = int(input("\n Escolha a coluna: "))

    while (coluna < 1 or coluna > 3):
        coluna = int(input("\n Escolha a coluna: "))
    coluna = coluna -1 # deixando coluna da vairvale linha na posição 0
           
    if lista[linha][coluna] == 0: #inserir numero na lista
        if jogador == 1:
            lista[linha][coluna] = 1 # numeros positivo para jogador X
        if jogador == 2:
            lista[linha][coluna] = -1 # numeros negativos para jogador O
    else:
        rodada = rodada -1 # -1 para retornar o jogador se prencher na linha ja com 1 ou -1
    
    rodada = rodada + 1 # passar para o jogador 2 na posição de resto da função 
    
    if rodada == 9: # empate se preencher tudo
        print("Empate ninguem ganhou")
        break                
    
# somando as linhas
    soma_linha = sum(lista[0])
    soma_linha01 = sum(lista[1])
    soma_linha02 = sum(lista[2])
# somando as colunas
    soma_coluna = lista[0][0] + lista[1][0] + lista[2][0]
    soma_coluna01 = lista[0][1] + lista[1][1] + lista[2][1]
    soma_coluna02 = lista[0][2] + lista[1][2] + lista[2][2]
#soma das diagonais
    diagonal = lista[0][0] + lista[1][1] + lista[2][2]
    diagonal02 = lista[0][2] + lista[1][1] + lista[2][0]

    if soma_linha == 3 or soma_linha01 == 3 or soma_linha02 == 3 or soma_coluna == 3 or soma_coluna01 == 3 or soma_coluna02 == 3 or diagonal == 3 or diagonal02 == 3: 
        vitoria = vitoria + 3  #vitória para X
    elif soma_linha == -3 or soma_linha01 == -3 or soma_linha02 == -3 or soma_coluna == -3 or soma_coluna01 == -3 or soma_coluna02 == -3 or diagonal == -3 or diagonal02 == -3:
        vitoria = vitoria - 3 # vitória para O
    if vitoria == 3:
        print(f'Parabêns ao jogador {jogador} pela vitória')
        break
    if vitoria == -3:
        print(f'Parabêns ao jogador {jogador} pela vitória')
        break
tela(lista)