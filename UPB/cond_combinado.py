"""
edad = int(input ("Digite su edad: "))
if edad >0:
    print("Edad correcta")
    if 0<edad<100: #if edad >=18 and edad<100:
        print("Usted es mayor de edad")
    else:
        print ("Usted es menor de edad")
else:
    print ("La edad es incorrecta")
"""
######################
"""
x = -2
if x>0:
    print ("X es positivo")
"""
#######################
"""
x = int(input("Digite valor de X: "))
y = int(input("Digite valor de Y: "))

if x < y:
    print ("X es menor que Y")
elif x > y:
    print ("X es mayor que Y")
else:
    print ("X es igual a Y")
"""
#######################

x = int(input("Digite valor de X: "))
y = int(input("Digite valor de Y: "))

if x == y:
    print ("X es menor que Y")
else:
    if x > y:
        print ("X es mayor que Y")
    else:
        print ("X es igual a Y")