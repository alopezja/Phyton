from os import system
system("clear")
print("Bienvenido al sistema de ubicación para zonas públicas WIFI”")
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
            menu = ["Cambiar contraseña", "Ingresar coordenadas actuales", "Ubicar zona wifi más cercana", "Guardar archivo con ubicación cercana", "Actualizar registros de zonas wifi desde archivo", "Elegir opción de menú favorita", "Cerrar sesión."]
            cont = 0
            while True:
                if cont >= 3:
                    print ("Error")
                    exit()
                for i in range(7):
                    print(str(i+1),". ",menu[i])
                try:
                    opcion = int(input("Elija una opción"))
                    if opcion < 1 or opcion > 7:
                        print("Error")
                        cont += 1
                    elif opcion == 6:
                        try:
                            favorita = int(input("Seleccione opción favorita"))
                            cont = 0
                            if favorita < 1 or favorita > 5:
                                print("Error")
                                exit()
                            else:
                                try:
                                    digito1 = int(input("Cantidad esquinas de un triángulo: "))
                                    if digito1 == 3:
                                        digito2 = int(input("Cuantos lados tiene un cuadrado:"))
                                        if digito2 == 4:
                                            favorita -= 1
                                            temporal = menu[favorita]
                                            menu.pop(favorita)
                                            menu.insert(0,temporal)
                                        else:
                                            print("Error")
                                    else:
                                        print("Error")
                                except ValueError:
                                    print("Error")
                        except ValueError:
                            print("Error")
                            exit()
                    elif opcion >=1 and opcion <=5:
                            print ("Usted ha elegido la opción "+str(opcion)+"")
                            exit()
                    elif opcion == 7:
                        print("Hasta pronto")
                        exit()
                except ValueError:
                    print("Error")
                    cont += 1
        else:
            system("clear")
            print("Error")
    else:
        system("clear")
        print("Error")
else:
    system("clear")
    print("Error")
