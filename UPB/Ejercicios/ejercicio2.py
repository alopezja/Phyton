try:
    gasto = int(input("Valor gastado:\n >>> "))
    if gasto<=0:
        print("El valor no es válido. Debe ingresar un valor mayor a 0")
    else:
        if 0<gasto<=100:
            print("Pago en efectivo")
        else:
            if 100<gasto<300:
                print("Pago con tarjeta débito")
            else:
                print("Pago con tarjeta de crédito")
except:
    print("Valor incorrecto")