matrizA = [
    [1, 2],
    [3, 4]
]

matrizB = [
    [5, 6],
    [7, 8]
]

# Verificar si las matrices tienen las mismas dimensiones
num_filas_A = len(matrizA)
num_filas_B = len(matrizB)
num_cols_A = len(matrizA[0])
num_cols_B = len(matrizB[0])
if num_filas_A == num_filas_B and  num_cols_A == num_cols_B :
    filas = len(matrizA)
    columnas = len(matrizA[0])
    matriz_suma = []

    for i in range(filas):
        fila_suma = []
        for j in range(columnas):
            fila_suma.append(matrizA[i][j] + matrizB[i][j])
        matriz_suma.append(fila_suma)

    print(matriz_suma)
else:
    print("Las matrices no tienen las mismas dimensiones para la suma.")