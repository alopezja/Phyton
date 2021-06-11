from os import system
system("clear")

# Listas con Append
print("\nAgregar elemento en lista")
t = [1,2,3,4]
t.append(5)
print(t)

# Listas con extend
print("\nLista con extend")
t1 = [1,2,3]
t2 = [4,5,6]
t1.extend(t2)
print(t1)

# Ordenar listas con sort
print("\nOrdenar listas con sort")
lista = ["b","d","k","a","c"]
lista.sort(reverse=True)
print(lista)

lista = [5,4,8,2,1]
lista.sort(reverse=True)
print(lista)

# Eliminar elementos con pop (Realmente no lo elimina sino que lo lleva a otra variable)
print("\nEliminar elementos con pop")
a = [1,2,3,4,["a","b"]]
x = a.pop(4)
print(a)
print(x)

"""
Métodos son singulares
lista: append, sort, reverse, pop, index, insert, clear (xxxx.clear)

Funciones son globales
len, numpy, del, random, max, min, sum >> num(xxxxx)

"""
#####################################
#Forma larga
print("\nForma larga")
lista2=[6,4,2,7,5,3,1,[1,2,3]]
print(lista2)                       #Imprime lista2
x=lista2.pop(7)
print(lista2)                       #Imprime lista2 sin la sublista
print(x)                            #Imprime la sublista
y=x.pop(1)                          #Elimna el índice 1 de la sublista
print(y)                            #Imprime la sublista sin el índice eliminado
lista2.extend([x])                  #A la lista2 le agrega la sublista sin en índice eliminado
print(lista2)                       #Imprime la nueva lista2

##############################
print("\nForma corta")
a = [6,4,2,7,5,3,1,[1,2,3]]
z = a[7].pop(1)
print(a)
print(z)

#Eliminar con del
print("\nEliminar con del")
t = [1,2,3]
del t[0]
print(t)

#Eliminar con remove
print("\nEliminar con remove")
t = [1,2,3]
t.remove(2)
print(t)

print("\nEliminar con remove elemento de sublista")
lista = [1,2,3,4,["a","b","c"]]
lista[4].remove("a")
print(lista)

#Rebanado
print("\nEliminar con del utilizando rebanado o rangos")
lista = [1,2,3,4,["a","b","c"]]
del lista[2:4]
print(lista)

#Funciones
print("\nFunciones")
num = [2,5,7,8,4,1,3,6]
print("Longitud",len(num))
print("Máximo",max(num))
print("Mínimo",min(num))
print("Suma",sum(num))
print("Promedio",sum(num)/len(num))