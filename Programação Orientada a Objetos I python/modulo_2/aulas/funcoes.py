def soma(a, b):
    
    return a + b


def cumprimenta_horario(nome, hora):
    
    if hora < 12:
        print("Bom dia,", nome)
    
    elif hora < 19:
        print("Boa tarde,", nome)
    
    else:
        print("Boa noite,", nome)
        
        
def calculadora(num1, num2):
    
    operacao = input("Digite a operação (+,-,*,/): ")
    
    if operacao == "+":

        resultado = num1 + num2

    elif operacao == "-":

        resultado = num1 - num2

    elif operacao == "*":

        resultado = num1 * num2

    elif operacao == "/":

        resultado = num1 / num2

    else: 

        resultado = "NÃO ENTENDI!"

    return resultado