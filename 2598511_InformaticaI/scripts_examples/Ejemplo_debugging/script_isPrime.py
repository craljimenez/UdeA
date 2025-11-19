def isPrime(x):
    '''Asume que x es un entero no negativo
    Retorna True si x es primo y Falso de lo contrario'''
    if x < 2:
        return False
    for i in range(2, x): # 2,1
        if x%i == 0:
            return False
    return True

# Probar con x = 2
if __name__ == "__main__":
    x = 2
    print(isPrime(x))
