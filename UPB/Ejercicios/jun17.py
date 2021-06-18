from os import system
system("clear")

dic = {'one':1,'two':2,'three':3,'varios':[1,2,3]}
print('one' in dic)
print(1 in dic)

value = list(dic.values())
print(1 in value)

value2 = list(dic.keys())
print(value2)

print("\n")

for clave in dic:
    print(clave,dic[clave]) #Se accede al elementro a través de la clave

print("\n")
dic = {'one':1,'two':2,'three':3}
for clave in dic:
    if dic[clave]>1:
        print(clave,dic[clave])


print("\n")
cont = {'chuck':1,'annie':42,'jan':100}
lst = list(cont.keys())
print(lst)
lst.sort()
for clave in lst:
    print(clave,cont[clave])

print("\n\nMétodos\n")

diccionario = {'Color':'Violeta','Talla':'M','Precio':50000}
diccionario.pop('Color')
print(diccionario)
diccionario.clear()
print(diccionario)

print("\n\nConvertir lista en dicionario\n")

secuencia = ['Color','Talla','Marca']
secuencia2 = ['Blanco','M','Lacoste']
diccionario1 = dict(zip(secuencia,secuencia2))
print(diccionario1)
#diccionarioFinal = (diccionario1.get(dict_keys()),diccionario2.get(dict_values()))
#print(diccionarioFinal)

print("\n\nCopiar diccionario\n")
diccionario = {'Color':'Violeta','Talla':'M','Precio':50000}
camiseta = diccionario.copy()
print(camiseta)

print("\n\nAgregar otro elemento\n")
camisa = {'Color':'Blanca','Marca':'Nike'}
camisa.setdefault('Talla',"M")
print(camisa)