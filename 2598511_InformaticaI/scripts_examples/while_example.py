
N = int(input("Ingrese un valor entero positivo: "))

i = 0 # iterador
while i<=N:
    i += 1 # incremento del iterador
    print("Esta es la iteración número", i)
    if i%2 == 0:
        print("El número es par")
        continue
    if i ==7:
        print("Rompiendo el bucle")
        break
    print("fin de la iteración")
    
print("Fin del bucle")