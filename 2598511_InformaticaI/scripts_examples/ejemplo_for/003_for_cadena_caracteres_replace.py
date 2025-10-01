"""
Se requiere un algoritmo que dada una cadena de caracteres,
por el usuario, le pida cambiar un caracter espécifico por otro. 
Ambos caracteres, de original y su remplazo, son dados por el usuario.
"""

"""
Entradas: string, caracter_origen y caracter_remplazo
salida: nueva string donde se remplaza el carcter de origen por el de remplazo.
"""

# Pedir datos de entrada al usuario
cadena = input("Ingrese el texto original:")
char_origen = input("Caracter a remplazar:")
char_remplazo = input("Caracter de remplazo:")

# Operaciones
"""
Cadenas de caracteres Inmutables, no se cambia su contenido una vez definido.
"""
"""
La suma es a dos números, lo que la concatenación es dos cádenas de caracteres.
"""
nueva_cadena = "" # inicializando la cadena de salida

for char in cadena:
    if char == char_origen:
        nueva_cadena = nueva_cadena + char_remplazo
    else:
        nueva_cadena = nueva_cadena + char

print("Salida:<",nueva_cadena,">",sep="")

