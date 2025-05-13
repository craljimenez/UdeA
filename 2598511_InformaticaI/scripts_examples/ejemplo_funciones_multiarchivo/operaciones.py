"""
Las funciones que realizan las operaciones de nuestra calculadora
"""

def suma(a, b):
    """
    Realiza la suma de dos números.

    Parámetros:
        a (float): Primer número.
        b (float): Segundo número.

    Retorna:
        float: La suma de a y b.
    """
    return a + b

def resta(a, b):
    """
    Realiza la resta de dos números.

    Parámetros:
        a (float): Primer número.
        b (float): Segundo número.

    Retorna:
        float: La resta de a menos b.
    """
    return a - b

def multiplicacion(a, b):
    """
    Realiza la multiplicación de dos números.

    Parámetros:
        a (float): Primer número.
        b (float): Segundo número.

    Retorna:
        float: El producto de a y b.
    """
    return a * b

def division(a, b):
    """
    Realiza la división de dos números.

    Parámetros:
        a (float): Numerador.
        b (float): Denominador.

    Retorna:
        float: El resultado de dividir a entre b.

    Lanza:
        ValueError: Si b es igual a 0.
    """
    if b == 0:
        raise ValueError("División por cero no es permitida.")
        # raise Warning("Division por 0")
    return a / b

def potencia(a, b):
    """
    Calcula la potencia de un número elevado a otro.

    Parámetros:
        a (float): Base.
        b (float): Exponente.

    Retorna:
        float: El resultado de a elevado a la potencia b.
    """
    return a ** b

def raiz_cuadrada(a):
    """
    Calcula la raíz cuadrada de un número.

    Parámetros:
        a (float): Número del cual se calculará la raíz cuadrada.

    Retorna:
        float: La raíz cuadrada de a.
    """
    if a < 0:
        raise ValueError(f"{a} no tiene raiz por ser un valor negativo.")
    return a ** 0.5