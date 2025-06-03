def create_matrix_identidad(filas,columnas):
    matriz_ceros = []

    for i in range(filas):
        fila = []
        for j in range(columnas):
            if i == j:
                fila.append(1)
            else:
                fila.append(0) # Inicializamos con ceros
        matriz_ceros.append(fila)
    return matriz_ceros


matriz_identidad = create_matrix_identidad(4,4)
print(matriz_identidad)