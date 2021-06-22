from os import system
system("clear")

# Tuplas
print("\nTuplas")
tupla = 1,2,3,4,5,6,7,8,9
tupla2 = (1,2,3,4,5)

print(tupla)
print(tupla2)

print("\nTupla de un elemento")
t = ("a",) #Para que sea una tupla es necesario poner la ,
print(t)
print(type(t))

print("\nTupla desde instrucción - Convertir a tupla")
#t1 = tuple([1,2,3])
t1 = tuple((1,2,3,4,5,6,7,8,9))
print(t1)
print(t1[0])
print(t1[1:4])
print(type(t1))
# t[0] = "A" #No es posible agregar elementos a las tuplas
# print(t1)

print("\nCrear nueva tupla desde otra")
tnew = ("A",) + t1[0:]
print (tnew)

print("\nTupla desde string")
t2 = tuple("Alex")
print(t2)

print("\nComparación de tuplas")
print((0,1,2)<(0,3,9))

print("\n")
m = ("Pásalo","bien")
x,y = m
print(x)
print(y)

print("\n")
a,b = "Seco","Sopa"
b,a = "Ensalada","Jugo"
a,b = b,a
print(a,b)
print(b,a)

print("\nDividir estructura")
direcc = 'alex@gmail.com'
usuario,dominio = direcc.split('@')
print(usuario)
print(dominio)

print("\nDiccionario de tuplas")
d = {'a':10,'b':1,'c':22}
t = list(d.items())
t.sort()
print(t)

print("\n")
tupla = (1,2,3,4,5)
print(tupla)
print(list(tupla))

lista = [1,2,3,4,5]
print(lista)
print(tuple(lista))

print("\nSuma de tuplas")
lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]
lista3 = lista1 + lista2
print(lista3)

tupla1 = (1,2,3,4,5)
tupla2 = (6,7,8,9,10)
tupla3 = (11,12,13,14,15)
tupla4 = tupla1 + tupla2 + tupla3
print(tupla4)

print("Mínimo de lista:",min(lista3))
print("Máximo de lista:",max(lista3))
print("Longitud de lista:",len(lista3))

print("Mínimo de tupla:",min(tupla4))
print("Máximo de tupla:",max(tupla4))
print("Longitud de tupla:",len(tupla4))