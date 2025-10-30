def print_matrix(M):
	for row in M:
		print(row)

def transpose_matrix(M):
	"""
	Transpone una matrix M
	M: Lista de listas (filas)
	retorna: M^T
	"""
	N = len(M) # Num Filas
	L = len(M[0]) # Num Col
	# validando que todas las filas tengan
	# El mismo número de elementos.
	for i in range(1,N):# 1,2,...,N-1
		if L != len(M[i]):
			raise ValueError("Todas las filas\
				deben tener la misma longiyud")
	M_T = []
	for j in range(L):
		new_row = []
		for i in range(N):
			new_row.append(M[i][j])
		M_T.append(new_row)
	return M_T

# Usando la funcion
Matrix = [[1,2,3],
		  [4,5,6]
		 ]

Matrix_transpuesta = transpose_matrix(Matrix)

print("Matriz Original:")
print_matrix(Matrix)

print("Matriz Transpuesta:")
print_matrix(Matrix_transpuesta)

#%%
print("Con numpy")
import numpy as np
M_np = np.array(Matrix)
print("Matrix transpuesta por numpy:")
print(M_np.T)