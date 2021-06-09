#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 18:35:30 2021

@author: exlonk
"""

print("Ingrese el valor de compra e ingrese un valor de cero para finalizar")

contador = 0
monto = None
numero_compra = 1

while monto != 0:
    monto= float(input("Valor compra {0}: ".format(numero_compra)))
    if monto > 0 :
        contador += monto 
        numero_compra +=1 
    elif monto < 0:
        print("Ingrese el valor correcto")
    else:
        break

if contador > 1000:
    contador = contador - contador*0.10
    print("Total compra:",contador)
else:
    print("Total compra:",contador)
