"""
Escribe una función llamada contar_vocales(cadena) 
que reciba una cadena de texto y devuelva el número total 
de vocales (a, e, i, o, u) en la cadena. Usa un bucle for
para recorrer cada carácter.
"""

"""
Entrada: es una cadena (string)
salida: entero que es número de vocales.
"""
cadena_base = "aeiouAEIOUÁÉÍÓÚáéíóúüÜ"

def contar_vocales_v1(cadena):
    num_vocales = 0
    for char in cadena: # range(i,j) i,i+1,i+2,i+3,...,j-1
        for letter in cadena_base:
            if char == letter:
                num_vocales += 1
                break
    return num_vocales

def contar_vocales_v2(cadena):
    global num_vocales
    num_vocales = 0
    for char in cadena: # range(i,j) i,i+1,i+2,i+3,...,j-1
        for letter in cadena_base:
            if char == letter:
                num_vocales += 1
                break

cadena = input("Ingresa Mensaje: ")

numero_vocales = contar_vocales_v1(cadena)
contar_vocales_v2(cadena)

print(f"Numero Vocales por v1: {numero_vocales}")
print(f"Numero Vocales por v2: {num_vocales}")



