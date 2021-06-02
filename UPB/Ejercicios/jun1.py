# While - True
"""
while True:
    linea = input("> ")
    if linea == "fin":
        break
    print (linea)
print("¡Terminado!")
"""
########################
"""
while True:
    linea = input("> ")
    if linea == "#":
        continue        #Salta a la siguiente iteración
    if linea == "fin":
        break
    print (linea)
print("¡Terminado!")
"""
########################
numero = 0
while numero < 10:
    numero = numero + 1
    if numero % 2 == 0:
        continue
    print (numero)

    