"""nombre=input("Digite su nombre: ")
edad=input("Digite su edad: ")

#print("Hola",nombre,"actualmente tienes",edad,"años")

#print("Hola {} actualmente tienes {} años".format(nombre,edad))

print(f"Hola {nombre} actualmente tienes {edad} años")
"""

# Switch

menu = """
       MENÚ
------------------
| 1 - SOPA       |
| 2 - SECO       |
| 3 - BEBIDAS    |
| 4 - POSTRES    |
| 5 - LICORES    |
------------------
"""
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
else:
    print("Debe seleccionar una opción correcta")
