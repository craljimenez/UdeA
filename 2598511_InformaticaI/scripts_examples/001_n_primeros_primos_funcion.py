#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  5 03:10:52 2025

@author: ubuntu-boxes
"""

#%%  Funciones
"""
Es un bloque de codigo (algoritmos), que puede tener:
    1. entradas
    2. Procesos (código)
    3. Salida

def nombre_funcion(entradas):
    ## Bloque de instrucciones, código
    
    return salidas
"""
def calcular_si_es_primo(num):
    h  = 2
    cont_factores = 0
    while h <= num//2:
        if num%h == 0:
            cont_factores +=1
        h += 1
    if cont_factores == 0:
        resultado  = True
    else:
        resultado = False
    return resultado
    

#%%

print("<Inicio Programa>")

N = input("Ingrese el número de números primos a imprimir:")

try:
    N = int(N)
except:
    print("Debe Ingresar un Entero")

i = 0
j = 1

while i<N:
    j_es_primo = calcular_si_es_primo(j)
    if j_es_primo:
        i += 1
        print(f"{i}-ésimo valor primo es {j}")
    else:
        pass
    j += 1

print("<Fin Programa>")