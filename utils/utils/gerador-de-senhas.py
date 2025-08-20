import random
import string

def gerar_senha(tamanho=12, usar_maiusculas=True, usar_minusculas=True, usar_numeros=True, usar_simbolos=True):
    caracteres = ''
    
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Selecione ao menos um tipo de caractere!")

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

if __name__ == "__main__":
    print("Gerador de Senhas Personalizadas")
    tamanho = int(input("Tamanho da senha (ex: 12): ") or 12)
    usar_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
    usar_minusculas = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
    usar_numeros = input("Incluir números? (s/n): ").lower() == 's'
    usar_simbolos = input("Incluir símbolos? (s/n): ").lower() == 's'

    try:
        senha = gerar_senha(tamanho, usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos)
        print("\nSenha gerada:", senha)
    except ValueError as e:
        print("Erro:", e)

#Adiciona gerador de senhas personalizadas na pasta utils#
