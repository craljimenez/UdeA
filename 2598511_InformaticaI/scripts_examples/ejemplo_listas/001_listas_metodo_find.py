mi_lista = [1,2,3,"hola",True]

print("Mi lista: ",mi_lista)

index = int(input("Ingrese index que desea adquirir: "))

elem = mi_lista.pop(index)

print(f"El elemento {elem} esta en la posición {index}")

print("mi_lista luego de .pop():",mi_lista)
