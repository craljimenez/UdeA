y = 10 # Variable Global
w = 19 # Global
def mi_funcion():
    global y
    y = 65  # Variable local
    print("Dentro de la función, y =", y)
    print(f"Dentro de la función, y + w ({y} + {w}) = ",y+w)

print("Fuera de la función antes de llamarla, y=",y)

mi_funcion()
print("Fuera de la función, y=",y)
# print("u = ",u)
# Esto generará un error porque 'y' no existe fuera de la función
# print("Fuera de la función, y =", y)