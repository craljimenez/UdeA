N = int(input("Ingrese N:")) #10
contador = 0
while contador < N: # 5 < 10
    contador = contador + 1 # 6
    if contador <= N-5: # 1 <= 5
        continue
    print(contador)
    print("------------")
print("<Fin del While>")