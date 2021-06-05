#Acumulador

from os import system
system("clear")
"""
total = 0
for valor in [2,4,6,8,10]:
    total = total + valor
    print(total)
print("El total es:",total)
"""
######################
mayor = None
print("Antes",mayor)
for valor in [20,4,60,8,100]:
    if mayor is None or valor > mayor:
        mayor = valor
    print("Bucle", mayor, valor)
print("El número mayor es:",mayor)

valor2 = [20,4,600,8,100]
print (max(valor2))