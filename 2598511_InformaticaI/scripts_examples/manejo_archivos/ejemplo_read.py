"""
En python existe el tipo de archivo "file"
El llamado de este tipo de archivos se hace por medio de la función
open(filepath,permisos)

permisos:
    r: lectura
    w: escritura (sobre escribe)
    a: append (agregar nuevo texto.)
"""

#%% Ejemplo read

file = open("./datos.txt")

# Recorriendo el archivo linea por linea
for row in file.readlines():
    print(row, end="")

# Mostrar una sola liena
file = open("./datos.txt")

print("\nNúmero de líneas: ", len(file.readlines()))
linea = int(input("¿Qué línea deseas leer? "))
file = open("./datos.txt")
linea_texto = file.readlines()[linea]
print("Linea extráida: ",linea_texto)
print("Tipo de la linea extráida:",type(linea_texto))