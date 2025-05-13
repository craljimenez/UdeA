"""Validar si la raiz cuadrada de un número dado es entera"""
from operaciones import raiz_cuadrada

num = int(input("Ingrese valor entero a validar:"))

raiz = raiz_cuadrada(num)

if raiz%1 == 0:
    print("La raiz cuadrada del valor",num,"es entero y es:",raiz)
else:
    print("La raiz cuadrada del valor",num,"no es entero y es:",round(raiz,4))
