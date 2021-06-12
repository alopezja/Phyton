from os import system
system("clear")

#Delimitadores para cambiar un string con un separador 
#para agregar cada argumento por separado a un elemento en una lista
s = "Alex-David-Lopez"
delimiter = "-"
print(s.split(delimiter))

lista = ["Programar","es","lo","mejor"]
delimiter = " "
print(delimiter.join(lista))

a = "casa"
b = "casa"
print(a is b) #Apuntan al mismo objeto

c = ["a","b","c"]
d = ["a","b","c"]

print(c is d) #Apuntan al diferente objeto

num = [1,2,3]
num2 = num
num2[0] = 0
print(num is num2)
print(num)

print("\n")
t1 = [1,2]
t2 = t1.append(3)
print(t1)
print(t2)

print("\n")
t1 = [1,2]
t3 = t1 + [3]
print(t1)
print(t3)
t2 is t3

print("\n")
a = [1,2]
a.insert(0,3)
print(a)
print(a.count(1))
a = [1,2,3,4,5,6,7,8,9]
print(a.index(3,0,8))