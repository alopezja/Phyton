                        coordenadas =[[0]*2 for i in range(3)]
                        for i in range(3):
                            for j in range(2):
                                try:
                                    if j == 0:
                                        coordenadas[i][j] = float(input("Digite la latitud para la coordenada "+str(i+1) +": "))
                                        coordenadas[i][j] = round(coordenadas[i][j],3)
                                        if coordenadas[i][j] > 6.306 or coordenadas[i][j] < 5.888:
                                            print("Error coordenada")
                                            exit()
                                        else:
                                            coordenadas[i][j] = float(input("Digite la longitud para la coordenada "+str(i+1) +": "))
                                            coordenadas[i][j] = round(coordenadas[i][j],3)
                                            if coordenadas[i][j] > -72.321 or coordenadas[i][j] < -72.552:
                                                print("Error coordenada")
                                                exit()
                                except ValueError():
                                    print("Error")
                                    exit()

                            for i in range(3):
                                print("coordenada [latitud,longitud] "+str(i+1)+" :", coordenadas[i])
                            print("la coordenada "+str(coordenadas.index(max(coordenadas))+"es la que está más al norte "))
                            latitud_promedio=0
                            longitud_promedio=0
                            for i in range(3):
                                for j in range(2):
                                    if j==0:
                                        latitud_promedio = latitud_promedio + coordenadas[i][j]
                                    else:
                                        longitud_promedio = longitud_promedio + coordenadas[i][j]
                            latitud_promedio /= 3
                            longitud_promedio /= 3
                            latitud_promedio = round(latitud_promedio,3)
                            longitud_promedio = round(longitud_promedio,3)
                            print("la coordenada promedio de todos los puntos [latitud,longitud] : [" + str (latitud_promedio)+ "," + str (longitud_promedio)+ "]")
                            try:
                                actualizar_coordenada = int(input("Presione 1,2 ó 3 para actualizar la respectiva coordenada. Presione 0 para regresar al menú"))
                                if actualizar_coordenada >= 1 and actualizar_coordenada <= 3:
                                    coordenadas[actualizar_coordenada - 1 [0]] = round(float(input("Digite la latitud para la coordenada "+ str(actualizar_coordenada))),3)
                                    if coordenadas [i][j] > 6.306 or coordenadas[i][j] < 5.888:
                                        print("Error coordenada")
                                        exit()
                                    
                                    coordenadas[actualizar_coordenada - 1 [1]] = round(float(input("Digite la longitud para la coordenada "+ str(actualizar_coordenada))),3)
                                    if coordenadas [i][j] > -72.321 or coordenadas[i][j] < -72.552:
                                        print("Error coordenada")
                                        exit()
                                elif actualizar_coordenada ==0:
                                    pass
                                else:
                                    print("Error actualización")
                                    exit()
                            except ValueError():
                                print("Error actualización")
                                exit()