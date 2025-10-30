file = open("datos.csv",mode="w")


file.write("nombre,edad,tipo_sangre\n")
while True:
    nombre = input("Ingrese nombre:")
    edad = input("Ingrese edad:")
    tipo_sangre = input("Ingrese tipo_sangre:")
    line = nombre+","+edad+","+tipo_sangre + "\n"

    file.write(line)

    respuesta = input("¿Quiere ingresar otro?si o no:")
    if respuesta == "no":
        break

file.close()

    



file.close()
