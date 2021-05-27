
try:
    ent = int(input("Digite la temperatura: "))
    farg = float(ent)
    cel = round((farg - 32.0)*5.0/9.0,2)
    print("En Gradis Celcius es: ",cel)
except:
    print("El valor ingresado no es correcto")


print("\n")


x=6
operador = "X es igual a 5" if x==5 else "X no es igual a 5"
print (operador)