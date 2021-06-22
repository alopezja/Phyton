from os import system
system("clear")

def muliplicar(a,b):
    print(a*b)

muliplicar(4,6)
muliplicar(5,5)
muliplicar(10,5)

print("\n")

def imprimir(x,y):
    print(x)
    print(y)
"""
x = input("Digite primer parámetro:")
y = input("Digite segundo parámetro:")

imprimir(x,y)
"""
imprimir("Hola","Como estás?")

def nombre_completo(nombre,apellido):
    print("Bienvenido:",nombre,apellido)

nombre = input("Digite primer parámetro: ")
apellido = input("Digite segundo parámetro: ")

nombre_completo(nombre,apellido)

print("\nParámetros arbitrarios")

def recorrer(param_fijo,*arbitrarios):
    print(param_fijo)
    for argumento in arbitrarios:
        print(argumento)

recorrer("Alex","Hola","Como estás?","Espero que muy bien")