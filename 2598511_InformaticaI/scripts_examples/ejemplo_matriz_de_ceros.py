def create_matrix_zeros(filas,columnas):
    matriz_ceros = []

    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(0) # Inicializamos con ceros
        matriz_ceros.append(fila)
    return matriz_ceros


matriz_ceros = create_matrix_zeros(3,4)
print(matriz_ceros)