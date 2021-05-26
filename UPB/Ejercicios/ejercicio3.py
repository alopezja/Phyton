###   Parque de diversiones
edad = int(input("Digite su edad:\n >>> "))

if 0<edad<18:
    print("Solo puede entrar a las atracciones de menores de edad")
else:
    if 18<=edad<60:
        print("Puede utilizar todas las atracciones del parque")
    else:
        if edad>=60:
            print("Solo puede utilizar unas cuantas atracciones")
        else:
            print("Digite una edad válida")