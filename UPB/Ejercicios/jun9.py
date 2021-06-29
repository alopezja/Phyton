from os import system
system("clear")
lista = ['Texto',1,5.5,['Texto',2]]
print(type(lista))
print(lista)

###########################################

quesos = ["Cheddar","Gouda","Parmessano"]
numeros = [1,2,3,4,[5,1]]
vacio = []
print(quesos,numeros,vacio)

# Lista mutable
print(quesos[0])
numeros[4][0] = 20
print(numeros)

# Mapeo
print("Gouda" in quesos)
print("Edan" in quesos)

# Recorrer lista
for queso in quesos:
    print("-> ",queso)

print("\n")
for i in range(len(numeros)):
    numeros[i] = numeros[i]*2
print(numeros)

###########################################
# Operadores con listas
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

d = [0]*2
print(d)

e = [1, 2, 3, 4, 5, 6]
e[2] = 10
print(e)

######################################
# Rebanado de listas

t=["a","b","c","d","e","f","g","h"]
print(t[1:3])
print(t[:5])
print(t[5:])