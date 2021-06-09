from os import system
bandera = True
system("clear")
menu = """
       MENÚ
--------------------------
| 1 - COMENZAR PROGRAMA   |
| 2 - IMPRIMIR LISTADO    |
| 3 - FINALIZAR PROGRAMA  |
--------------------------
"""

while bandera:
    print(menu)
    operacion = int(input("Por favor seleccione la opción de su agrado: "))
    if operacion is 1:
        print("Usted ha seleccionado la opción 1")
    elif operacion is 2:
        print("Usted ha seleccionado la opción 2")
    elif operacion is 3:
        print("PROGRAMA FINALIZADO")
        break
    else:
        print("Debe seleccionar una opción correcta")
