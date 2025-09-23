# Usuario ingresa numeros, decir si son pares o impares, si ingresa un número negativo debe finalizar

while True: # 0 == 0
    n = int(input("Ingrese valor:"))
    if n < 0:
        break
    if n%2 == 0:
        print("\tRes// el número es Par.")
    else:
        print("\tRes// el número es Impar.")

print("<Fin del While>")
