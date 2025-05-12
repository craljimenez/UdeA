
file = open("./datos.txt", "w")

# Escribir en el archivo
file.write("Nuevo Contenido del archivo\n")

file.close()
print("Escribí en el archivo")

file = open("./datos_v2.txt", "w")

file.write("Nombre,Edad2,Apellidos,Nota,Observaciones\n")
file.write("Cristian,32,Jimenez Castaño,3.0,N/A\n")
file.write("Alfonso,32,Jimenez Castaño,3.0,N/A\n")


file.close()