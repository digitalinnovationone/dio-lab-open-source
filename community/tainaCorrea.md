Olá Eu sou a Tainá Corrêa 👋
Sou apaixonada por Programação, me Destaco no Front End, 
Estou muito animada com esse Bootcamp em Python, uma linguagem poderosa, vou me dedicar para aprender e abstrair tudo o conhecimento do Curso!!

//LET`S GO PYTHON =)
import time

mensagem = "Vai ser emocionante essa trilha em Python Com a DIO.me  Tainá Correa ;)"
def limpar_tela():
    print("\033[H\033[J", end='')

def exibir_animacao(mensagem):
    for i in range(len(mensagem)):
        limpar_tela()
        print(mensagem[:i+1])
        time.sleep(0.1)  

exibir_animacao(mensagem)
