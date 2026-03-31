#Eduardo

#Código usando if,elif e else em python 

x = 2
y = 5
z = 0
resultado = 0
valor = int(input('Digite 1, 2 ou 3: '))
if valor ==1:
   resultado = x * valor
   valor = 2
elif valor ==2:
   resultado = y * valor

elif valor ==3:
   resultado = z * valor
else:
   print('Você digitou um valor inválido')
print(resultado)
