#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  5 03:10:52 2025

@author: ubuntu-boxes
"""
print("<Inicio Programa>")

N = input("Ingrese el número de números primos a imprimir:")

try:
    N = int(N)
except:
    print("Debe Ingresar un Entero")

i = 0
j = 1

while i<N:
    h = 2
    cont_factores = 0
    while h <= j//2:
        if j%h == 0:
            cont_factores += 1 # cont_factores = cont_factores + 1 
        else:
            pass
        h += 1
    if cont_factores == 0:
        i += 1
        print(f"{i}-ésimo valor primo es {j}")
    else:
        pass
    j += 1

print("<Fin Programa>")
        
        