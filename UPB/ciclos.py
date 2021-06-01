#Ciclos
from os import system
"""
n = 5
while n > 0:
    print (n)
    n = n - 1
print ("<<< Despegar >>>")
"""
#####################
"""
i=0
while i<=3:
    print (i)
    i=i+1
print ("Hecho")
"""
#####################
"""
año = 2001
while año <= 2021:
    print("Informe del año ",año)
    año = año + 1
 """
 ####################
"""
bandera = True
system("clear")
while bandera:
    nombre = input("Indique su nombre: ")
    if nombre:
        break
"""
#######################
bandera = True
system("clear")
menu = """
       MENÚ
------------------
| 1 - SOPA       |
| 2 - SECO       |
| 3 - BEBIDAS    |
| 4 - POSTRES    |
| 5 - LICORES    |
------------------
PARA SALIR DEL MENÚ DIGITE 0
"""
while bandera:
    print(menu)
    operacion = int(input("Por favor seleccione la opción de su agrado: "))
    if operacion is 1:
        print("Sopa de queso\nSancocho de gallina\nSopa de pescado\nAjiaco\nSopa de mondongo")
    elif operacion is 2:
        print("Arroz de coco\nArroz de pollo\nArroz de cangrejo\nArroz con espinaca")
    elif operacion is 3:
        print("Guarapo\nLimonada\nClaro\nGaseosa\nMasato")
    elif operacion is 4:
        print("Tres leches\nLimón\nMilo\nOreo\nMaracuyá")
    elif operacion is 5:
        print("Ron Medellín\nVino\nWiskey\nCerveza\nAguardiente\nTequila")
    elif operacion is 0:
        print("Gracias por visitarnos")
        break
    else:
        print("Debe seleccionar una opción correcta")
