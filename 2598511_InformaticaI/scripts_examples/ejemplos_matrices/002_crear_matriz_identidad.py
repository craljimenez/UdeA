def print_matrix(M):
    for row in M:
        print(row)

def create_identity_matrix(D):
    """
    Crear una matriz identidad cuadrada de dimensión D.
    """
    matrix = []
    for row in range(D):
        vector_row = []
        for column in range(D):
            if row == column: # ¿Estoy en la diagonal?
                vector_row.append(1)
            else:
                vector_row.append(0)
        matrix.append(vector_row)
    
    return matrix

try:
    D = int(input("Ingrese dimensión de la matriz identidad a crear: "))
except Exception as e:
    raise ValueError(f"Debe de ingresar un valor entero.\nError de Python: {e}")

matriz_identidad = create_identity_matrix(D)

print("Matriz Generada:")
print_matrix(matriz_identidad)

