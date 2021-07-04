from os import system
import os
from math import sin,cos,asin,sqrt,radians,degrees
system("clear")

x = 51634
y = 43615
coordenada = []
listaDistancias = []
radio = 6372.795477598
coordenadaPrueba =  [[6.250,-72.450],
                    [6.202,-72.402],
                    [6.204,-72.404]]

listaPredefinida =  [[6.211,-72.482,2],
                    [6.212,-72.470,25],
                    [6.105,-72.342,25],
                    [6.210,-72.442,50]]

def ingresarCoordenada (coordenadaInicial):
    coordenadaDuplicada = list(coordenadaInicial)
    for x in range (0,3):
        coordenadaDuplicada.append([])
        lat = input("Ingrese la latitud: ")
        while lat == "" or lat == " ":
            print("Error")
            exit()
        lat = float(lat)
        if lat <= 6.306 and lat >= 5.888:
            lon = input("Ingrese la longitud: ")
            while lon == "" or lon == " ":
                print("Error")
                exit()
            lon = float(lon)
            if lon <= -72.321 and lon >= -72.552:
                coordenadaDuplicada[x].insert(0,lat)
                coordenadaDuplicada[x].insert(1,lon)
            else:
                print("Error coordenada")
                exit()
        else:
            print("Error coordenada")
            exit()
    print("Coordenadas ingresadas correctamente")
    return coordenadaDuplicada

def ordenarLatitudes(coordenadaInicial):
    print(f"La coordenada que está mas al sur es: {min(coordenadaInicial, key=lambda posicion:posicion[0])}")
    #print(f"La coordenada que está mas al norte es: {max(coordenadaInicial, key=lambda posicion:posicion[0])}")
"""
def ordenarLongitudes(coordenadaInicial):
    print(f"La coordenada que está mas al oriente es: {max(coordenadaInicial, key=lambda posicion:posicion[1])}")
    print(f"La coordenada que está mas al occidente es: {min(coordenadaInicial, key=lambda posicion:posicion[1])}")
"""
def promedioCoordenadas(coordenadaInicial):
    print(f"El promedio de los puntos es: ['{(coordenadaInicial[0][0]+coordenadaInicial[1][0]+coordenadaInicial[2][0])/3}','{(coordenadaInicial[0][1]+coordenadaInicial[1][1]+coordenadaInicial[2][1])/3}'']")
    """
    print(f"El promedio de las latitudes es: {(coordenadaInicial[0][0]+coordenadaInicial[1][0]+coordenadaInicial[2][0])/3}")
    return
    print(f"El promedio de las longitudes es: {(coordenadaInicial[0][1]+coordenadaInicial[1][1]+coordenadaInicial[2][1])/3}")
    """

def imprimirCoordenada(coordenadaInicial):
    coordenadaDuplicada=list(coordenadaInicial)
    print("Las coordenadas guardadas actualmente son:")
    for x in range(0,len(coordenadaDuplicada)):
        print(f"{x+1}. Coordenada [Latitud,Longitud]: ['{coordenadaDuplicada[x][0]}', '{coordenadaDuplicada[x][1]}']")
    ordenarLatitudes(coordenadaDuplicada)
    #ordenarLongitudes(coordenadaDuplicada)
    promedioCoordenadas(coordenadaDuplicada)
    choice=int(input("Presione 1,2 ó 3 para actualizar la respectiva coordenada. Presione 0 para regresar al menú: "))
    if choice == 0:
        return
    elif choice!=1 and choice!=2 and choice!=3:
        print("Error actualización")
        exit()
    else:
        actualizarCoordenadas(choice,coordenadaInicial)

def actualizarCoordenadas(choice, coordenadaInicial):
    coordenadaDuplicada = list(coordenadaInicial)
    choice=choice-1
    lat = input("Ingrese la latitud: ")
    while lat == "" or lat == " ":
        print("Error")
        exit()
    lat = float(lat)
    if lat <= 6.306 and lat >= 5.888:
        lon = input("Ingrese la longitud: ")
        while lon == "" or lon == " ":
            print("Error")
            exit()
        lon = float(lon)
        if lon <= -72.321 and lon >= -72.552:
            coordenadaDuplicada[choice][0]=lat
            coordenadaDuplicada[choice][1]=lon
        else:
            print("Longitud fuera del rango")
            coordenadaDuplicada=[coordenadaInicial] #En caso de error retornamos la lista original (sin cambios)
            return coordenadaDuplicada
    else:
        print("Latitud fuera del rango")
        coordenadaDuplicada=[coordenadaInicial] 
        return coordenadaDuplicada
    
    return coordenadaDuplicada #En caso éxito retornamos la nueva lista

def mostrarRestauranteFav(coordenadaInicial):
    if coordenadaInicial==[]:
        print("No hay restaurantes favoritos ingresados")
        exit()
    else:
        imprimirRestauranteFav(coordenadaInicial)

def imprimirRestauranteFav(coordenadaInicial):
    coordenadaDuplicada=list(coordenadaInicial)
    print("Las coordenadas guardadas actualmente son:")
    for x in range(0,len(coordenadaDuplicada)):
        print(f"{x+1}. Coordenada [Latitud,Longitud]: ['{coordenadaDuplicada[x][0]}', '{coordenadaDuplicada[x][1]}']")
    opcion=int(input("Por favor seleccione restaurante actaual: "))
    if opcion == 1 or opcion == 2 or opcion == 3:
        prepararDatos(opcion,coordenadaDuplicada,listaPredefinida)
    else:
        print("Restaurante no existe")

def prepararDatos(indRestActual, coordinadaInicial, coordFijas):
    listaDuplicada = list(coordinadaInicial)
    listaDuplicadaFija = list(coordFijas)
    lat1 = listaDuplicada[indRestActual-1][0]
    lon1 = listaDuplicada[indRestActual-1][1]
    lat1 = convertirRadianes(lat1)
    lon1 = convertirRadianes(lon1)
    for x in range (0,len(listaDuplicadaFija)):
        for y in range (0,2):
            listaDuplicadaFija[x][y] = convertirRadianes(listaDuplicadaFija[x][y])
    
    formulaDistancia(lat1,lon1,listaDuplicadaFija)

    pass

def convertirRadianes(valorConvertir):
    return radians(valorConvertir)
    pass

def formulaDistancia(lat1, lon1, listaRadianes):

    for x in range(0,4):
        lat2 = listaRadianes[x][0]
        lon2 = listaRadianes[x][1]
        latDelta = lat2 - lat1
        lonDelta = lon2 - lon1

        aux = sin(lonDelta/2)**2
        aux = aux*(cos(lat1)*cos(lat2))
        aux = (sin(latDelta/2)**2)+aux 
        aux = sqrt(aux)
        aux = asin(aux)
        aux = (2*radio)*aux
        aux = aux*1000

        listaDistancias.append(aux)

    ordenarDistancias(listaDistancias)

def ordenarDistancias(distancias):
    distanciasDuplicadas = list(distancias)
    min1 = distanciasDuplicadas.index(min(distanciasDuplicadas))
    distanciasDuplicadas.pop(min1)
    min2 = distancias.index(min(distanciasDuplicadas))
    imprimirMensajeCerca(min1,min2,listaPredefinida)
    

def imprimirMensajeCerca(min1,min2,baseDatos):
    for x in range(0,4):
        baseDatos[x][0] = degrees(baseDatos[x][0])
        baseDatos[x][1] = degrees(baseDatos[x][1])
    if baseDatos[min1][2] > baseDatos[min2][2]:
        print(f"1. El restaurante más cercano está en la latitud: '{baseDatos[min1][0]}' longitud: '{baseDatos[min1][1]}', está a {listaDistancias[min1]} metros y tiene {baseDatos[min1][2]} platos")
        print(f"2. El siguiente restaurante está en la latitud: '{baseDatos[min2][0]}' longitud: '{baseDatos[min2][1]}', está a {listaDistancias[min2]} metros y tiene {baseDatos[min2][2]} platos")
    else:
        print(f"1. El restaurante más cercano está en la latitud: '{baseDatos[min2][0]}' longitud: '{baseDatos[min2][1]}', está a {listaDistancias[min2]} metros y tiene {baseDatos[min2][2]} platos")
        print(f"2. El siguiente restaurante está en la latitud: '{baseDatos[min1][0]}' longitud: '{baseDatos[min1][1]}', está a {listaDistancias[min1]} metros y tiene {baseDatos[min1][2]} platos")

mostrarRestauranteFav(coordenadaPrueba)

#?#################################################################################
"""
print("Bienvenido al sistema de ubicación para zonas públicas WIFI”")
usuario = int(input("Digite el usuario: "))
if usuario == x:
    system("clear")
    contraseña = int(input("Digite la contraseña: "))
    if contraseña == y:
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
                    elif opcion == 1:
                        claveAnterior = int(input("Digite la contraseña anterior: "))
                        if y != claveAnterior:
                            print("Error")
                            exit()
                        else:    
                            nuevaClave = int(input("Digite la nueva contraseña: "))
                            while nuevaClave == y:
                                print("Error")
                                nuevaClave = int(input("Digite la nueva contraseña: "))    
                            nuevaClave2 = int(input("Confirmar nueva contraseña: "))
                            if nuevaClave == nuevaClave2:
                                y = nuevaClave
                                print("Cambio de contraseña exitoso")
                            else:
                                print("Error")
                    elif opcion == 2:
                        if coordenada==[]:
                            coordenada = ingresarCoordenada(coordenada)
                        else:
                            imprimirCoordenada(coordenada)
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
    """