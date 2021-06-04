# Creación de listas
from os import system
system("clear")
"""
alex = ["Alex",33,True,1.75]
print(type(alex))
"""
########################
"""
lenguajes = ["Python","C++","C#","PHP","Java"]
print(lenguajes[-3])
"""
#######################
"""
amigos = ["Juan", "Pedro", "Carlos"]
for amigo in amigos:
    print("Feliz año nuevo",amigo)
print ("Terminado")
"""
#######################
"""
lista = ["Juan", "Antonio", "Pedro", "Luis"]
for nombre in lista:
    print(nombre)
"""
#########################

for año in range (2001, 2013):
    print ("Informes del año:", año)

for año in range (2013, 2001, -1):
    print ("Informes del año:", año)