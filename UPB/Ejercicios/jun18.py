from os import system
system("clear")

diccionario1 = {'Color':'Violeta','Talla':'M'}
diccionario2 = {'Precio':50000,'Marca':'Nike'}
diccionario1.update(diccionario2)
print(diccionario1)

print(diccionario1.get('Color'))
print(diccionario1['Color'])

print("\n")
diccionario = {'Color':'Violeta','Marca':'Nike','Talla':'M'}
for clave,valor in diccionario.items():
    print("La clave",clave,"es:",valor)

print("\n")
for k,v in diccionario.items():
    print("La clave",k,"es:",v)

print(diccionario.keys())
print(diccionario.values())

# Tuplas
print("\nTuplas")
tupla = 1,2,3,4,5,6,7,8,9
tupla2 = (1,2,3,4,5)

print(tupla)
print(tupla2)