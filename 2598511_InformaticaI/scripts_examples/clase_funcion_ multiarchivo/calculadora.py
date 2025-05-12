"""
Ejemplo de calculadora con funciones multiarchivo
Creado por: Cristian Informática I 2025-I
"""
# import funciones.utils as alias # 1ra forma, se debe usar el alias o el nombre del import para llamar las funciones de aquel archivo.

# from funciones.utils import suma,\
#                             resta,\
#                             division,\
#                             multiplicacion,\
#                             potencia,\
#                             raiz_cuadrada # PAra importar todo, en vez de enlistar todas las funciones se usa el comodían *

from funciones.utils import *

# import funciones.utils.suma as sum 



print("""
Opción\t Descripción
a\t Suma
b\t Resta
c\t Multiplicación
d\t División
e\t Potencia
f\t Raiz Cuadrada
""")
opcion = input("Ingrese Operación: ")
opcion = opcion.lower()

a = float(input("Ingrese el primer número: "))
if opcion != "f":
    b = float(input("Ingrese el segundo número: "))

if opcion == 'a':
    print(f"Suma {a}+{b} = {suma(a,b)}")
elif opcion=='b':
    print(f"Resta {a}-{b} = {resta(a,b)}")
elif opcion=='c':
    print(f"Multiplicación {a}*{b} = {multiplicacion(a,b)}")
elif opcion=='d':
    print(f"División {a}/{b} = {division(a,b)}")
elif opcion=='e':
    print(f"Potencia {a}^{b} = {potencia(a,b)}")
elif opcion=='f':
    print(f"Raiz Cuadrada de {a} = {raiz_cuadrada(a)} ")
else:
    raise ValueError("Opcíon no válida.")