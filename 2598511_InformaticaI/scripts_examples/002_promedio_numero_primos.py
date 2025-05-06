#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  5 17:43:02 2025

@author: ubuntu-boxes
"""

"""
Script que recibe numeros enteros positivos del usuario
y cuando recibe un valor impar, imprime el promedio que se lleva hasta el momento
de los valores impares. Cuando reciba un valor primo, debe notificarse que es primo.

El programa fnaliza cuando el usuario ingresa el valor de 0.
"""

contador_impares = 0
sum_impares = 0

while True:
    n = int(input("Ingrese un valor entero positivo:"))
    # Si el valor es negativo
    if n < 0:
        print("¡Ojo, números enteros positivos!")
        continue
    if n == 0:
        print("Finalizaste")
        break
    
    if n%2 == 0: # Verificando si es par
        pass
    else: # solo entra si es impar
        contador_impares += 1 # contador_impares = contador_impares + 1 
        sum_impares += n
        prom_impares = sum_impares/contador_impares
        print("El promedio de # impares hasta el momento es: ",prom_impares)
    
    # validar si es primo
    h = 2
    contador_factores = 0
    while h <= n//2:
        if n%h == 0:
            contador_factores += 1
        h += 1
    if contador_factores == 0:
        print(f"\t{n} es primo")
#Fin While principal.