def print_matrix(M):
    for row in M:
        print(row)

def create_matrix_zeros(filas,columnas):
    """
    crea una matriz de ceros de tamaño filas x columnas
    """
    matriz_ceros = [] # list()

    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(0) # Inicializamos con ceros
        matriz_ceros.append(fila)
    return matriz_ceros


matriz_ceros = create_matrix_zeros(3,4)
print_matrix(matriz_ceros)