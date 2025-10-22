# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import sys

file = open("./archivo_externo.txt",
            mode="r",
            encoding="utf8"
            ) # apuntado file al archivo.
print(f"El tamaño del archibo\
      es: {sys.getsizeof(file)}")

# string = file.read() # leer el archivo y guardando su contenido en string

lines = file.readlines()

# print("string:\n",string,sep="")
# print("lines:\n",lines,sep="")

anio = []
cod = []
titulo = []



for row in lines[1:]:
    campo = ""
    num_comma = 0
    row += ","
    for char in row:
        if char != ",":
            campo += char
        else:
            if num_comma==0:
                anio.append(campo)
            elif num_comma == 1:
                titulo.append(campo)
            elif num_comma == 2:
                cod.append(campo)
            else:
                raise ValueError("No se tinene encuenta más campos, falla en el formato del archivo.")
            campo = ""
            num_comma += 1

for i in range(len(anio)): # 0,1,2, ..., N-1
    anio[i] = int(anio[i])


for i in range(len(cod)): # 0,1,2, ..., N-1
    campo = ""
    for char in cod[i]:
        if char!="\n":
            campo += char
    cod[i] = campo

sorted_anio = anio.copy()
sorted_anio.sort()

ind_sort = []
for i in range(len(sorted_anio)):
    aux_anio = anio.copy() # Copia de anio, evitando el aliasing
    
    count_in_anio = anio.count(sorted_anio[i])  
    count_in_anio_sorted = sorted_anio[:i].count(sorted_anio[i]) # Se cuentas cuanta veces esta el elemento sorted_anio[i] en la sublista que ha sido procesada de sorted_anio
    if (count_in_anio - count_in_anio_sorted) > 0: # Si existen anios repetidos, entra al if.
        for _ in range(count_in_anio_sorted): # Se remueve el elemento en aux_anio tantas veces como las veces que se ha procesado hasta el momento de la iteracción i-ésima.
            aux_anio.remove(sorted_anio[i])

    idx = aux_anio.index(sorted_anio[i]) # index en aux_anio donde esta el actual elemento.
    factor = count_in_anio - (count_in_anio - count_in_anio_sorted) # Factor por repetición, si existen repetido se suma al index posiciones eliminadas anteriormente.

    ind_sort.append(idx + factor) 

print("ind_sort:",ind_sort)

file_destino = open("./archivo_ordenado_por_anio.csv",mode="w")


#file_destino.close()


#file_destino = open("./archivo_ordenado_por_anio.csv",mode="a")
file_destino.write(lines[0])
for idx in ind_sort:
    line = str(anio[idx])+","+titulo[idx]+","+cod[idx]+"\n"
    file_destino.write(line)

file_destino.close()    
