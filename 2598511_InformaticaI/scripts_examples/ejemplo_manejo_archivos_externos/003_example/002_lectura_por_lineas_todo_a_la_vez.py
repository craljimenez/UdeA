file = open("./texto.txt",mode="r")

lista_lineas = file.readlines()

print("len(lista_lineas):",len(lista_lineas))
print("lista_lineas[0]:",lista_lineas[0])
print("lista_lineas[1]:",lista_lineas[1])




file.close()