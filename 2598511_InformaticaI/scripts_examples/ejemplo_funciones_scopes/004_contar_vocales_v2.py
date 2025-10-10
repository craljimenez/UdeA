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
def dentro(char,cadena):
    """
    True si char esta dentro de cadena, y un False si esta afuera.
    """
    response = False
    for letter in cadena:
        if char == letter:
            response = True
            break
    return response
            
def contar_vocales(cadena):
    num_vocales = 0
    for char in cadena: # range(i,j) i,i+1,i+2,i+3,...,j-1
        if dentro(char,cadena_base):
            num_vocales += 1
    return num_vocales

cadena = input("Ingresa Mensaje: ")

numero_vocales = contar_vocales(cadena)

print(f"Numero Vocales: {numero_vocales}")