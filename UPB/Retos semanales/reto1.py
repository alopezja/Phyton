from os import system
print("Bienvenido al sistema de ubicación para zonas públicas WIFI”")
try:
    usuario = int(input("Digite el usuario: "))
    if usuario == 51634:
        system("clear")
        contraseña = int(input("Digite la contraseña: "))
        if contraseña == 43615:
            system("clear")
            termino1=634
            termino2=(((1+2)*2)-3)
            captcha = str(print(termino1," + ",termino2,"=",))
            valor=str(input())
            if valor==str((termino1+termino2)):
                system("clear")
                print("Sesión iniciada")
            else:
                system("clear")
                print("Error")
        else:
            system("clear")
            print("Error")
    else:
        system("clear")
        print("Error")
except:
    print("Error")