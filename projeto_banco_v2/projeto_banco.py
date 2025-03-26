entradas = input("")
print(entradas.split(","))

# Aplique a função map(int, ...) para converter cada elemento dessa lista de strings em um inteiro.
entradass = map(int, entradas)
print(entradass)

# Usar a função list() para converter o objeto map resultante em uma lista de inteiros.