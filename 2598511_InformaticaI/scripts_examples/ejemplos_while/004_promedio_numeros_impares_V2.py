"""
El algoritmo va leyendo consecutivamente números enteros del usuario
y va imprimiendo el promedio de los números impares que ha ingresando.
El algortimo termina cuando el usuario ingresa un valor negativo.
"""
# Inicializar los iteradores
sum_impares = 0 # Iterador acumular
cont_impares = 0 # Iterador Contador

# for NO es una buena alternativa

while True:
    N = input("Ingrese Valor Entero:") # N será de tipo string
    N = int(N) # int() convierte su argumento en un número entero, si es posible

    if N >= 0: # Valor a procesar
        if N%2 == 0: # N es parpass
            pass # No haga nada
        else: # N es Impar
            # hay que calcular promedio
            sum_impares = sum_impares + N # sum_impares += N
            cont_impares = cont_impares + 1
        if cont_impares != 0:
            promedio_impares = sum_impares/cont_impares
        else:
            promedio_impares = 0.0
        promedio_redondeado = round(promedio_impares,2)
        print("Promedio de Imapares: ",promedio_redondeado)
    else: # N es negativo
        break

print("<FIN PROGRAMA>")


