"""
Algoritmo que indica si un número es primo o no
"""
N = input("Ingrese valor a validar:") # N es string
N = int(N) # Convierte N a entero.

# N = int(input("Ingrese valor...:"))

a = N//2 # Division entera
num_divisores = 0
for factor in range(2,a+1): # 2,3,4,...,a
    if N%factor == 0: # Si N es divisible por factor
        num_divisores += 1 # num_divisores = num_divisores + 1
# Fin del for
if num_divisores != 0:
    print(N,"no es primo")
else:
    print(N,"es primo")



