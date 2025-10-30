file = open("datos.csv",mode="a") # r: lectura, w: escritura, a:append, x: crear el acrivoy escribir.

while True:
    nombre = input("Ingrese Nombre: ")
    edad = input("Ingrese Edad: ")
    tipo_sangre = input("Ingrese RH+: ")
    line = f"{nombre},{edad},{tipo_sangre}\n"
    file.write(line)

    answer = input("¿Deseas ingresar un nuevo registro? (si/no)")
    if answer == "no":
        break

file.close()
