import random

def jogo_par_ou_impar():
    print("Bem-vindo ao jogo de Par ou Ímpar!")
    print("Escolha sua opção:")
    print("1 - Par")
    print("2 - Ímpar")
    
  # Solicita a escolha do usuário e valida a entrada
  while True:
        try:
   escolha = int(input("Digite 1 para Par ou 2 para Ímpar: "))
  if escolha not in [1, 2]:
                print("Opção inválida! Tente novamente.")
  else:
        break
   except ValueError:
            print("Entrada inválida! Digite um número (1 ou 2).")
    
   # Solicita um número para o usuário
   try:
        numero_usuario = int(input("Digite um número: "))
   except ValueError:
        print("Entrada inválida! Digite um número inteiro.")
        return
    
   # O computador escolhe um número aleatório entre 1 e 10
   numero_computador = random.randint(1, 10)
    soma = numero_usuario + numero_computador

   print(f"\nVocê jogou: {numero_usuario}")
    print(f"O computador jogou: {numero_computador}")
    print(f"A soma é: {soma}")
    
   # Verifica se a soma é par ou ímpar
   if soma % 2 == 0:
        resultado = 1  # Representa Par
        print("O resultado é Par!")
  else:
        resultado = 2  # Representa Ímpar
        print("O resultado é Ímpar!")
    
  # Determina o vencedor
  if escolha == resultado:
      print("\nParabéns! Você venceu!")
  else:
        print("\nQue pena, você perdeu!")

if __name__ == "__main__":
    jogo_par_ou_impar()
