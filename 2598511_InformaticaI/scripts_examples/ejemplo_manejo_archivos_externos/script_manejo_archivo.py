
"""
función open(filepath,permisos)
filepath: Ruta de Archivo (leer o escribir o sobreescribir)
permisos: leer (r), sobreescribir (w) y append/escribir (a)
"""
file = open("./archivo_texto.txt", "r") # /home/craljimenez/Documents/Reposirorio_craljimenez/UdeA/2598511_InformaticaI/scripts_examples/ejemplo_manejo_archivos_externos/archivo_texto.txt
# primera_fila = file.readline() # Lee primera Fila
texto = file.readlines() # Lee todas las filas que no han sido leídas

# print("primera fila:",primera_fila)
print("texto:",texto)

print("primera linea",file.readline())

# Volviendo a cargar el archivo

print("*************** Volviendo a cargar el archivo ***************")
file = open("archivo_texto.txt",'r')
filas_file = file.readlines()
num_filas = len(filas_file)
i = 0
while i<num_filas:
    print(f"Fila {i+1}: ",filas_file[i],end="")
    i +=1
print("\n")

file.close()
## Escribir

file_write = open("archivo_texto.txt",'w')
file_write.write("Hola Pues, sobre escribimos\n")
file_write.write("Esto es una nueva fila desde la sobreescrita\n")

file_write.close()


# Crear archivos nuevos desde python

new_file = open("./data/nuevo_archivo_ejemplo.txt","w")
new_file.write("Primera Fila\n")
new_file.write("""Esto es un contenido
amplio de ejemplo
""")
new_file.close()

# Append (escribir sobre el archivo existente, desde su final)

appended_file = open("./data/nuevo_archivo_ejemplo.txt","a")
appended_file.write("Esta es una nueva linea desde append\n")
appended_file.write("Esta es otra nueva linea desde append\n")


appended_file.close()