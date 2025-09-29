n = 0
while True:
    n = int(input("Ingrese un numero (0 para salir): "))
    if n == 0:
        print("Programa finalizado.")
        break
    if n > 1:
        for i in range(2, n//2+1):
            if (n % i) == 0:
                print(n, "no es un numero primo")
                break
        else:
            print(n, "es un numero primo")
    else:
        print("Ingrese un número mayor que 1 para verificar si es primo.")