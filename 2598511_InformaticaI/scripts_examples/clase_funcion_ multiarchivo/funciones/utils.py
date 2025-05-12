"""
Name: funciones utiles
creado por: Cristian Informática I 2025-I
"""

def suma(a, b):
    """
    Suma dos números
    :param a: primer número
    :param b: segundo número
    :return: suma de a y b
    """
    return a + b
def resta(a, b):
    """
    Resta dos números
    :param a: primer número
    :param b: segundo número
    :return: resta de a y b
    """
    return a - b
def multiplicacion(a, b):
    """
    Multiplica dos números
    :param a: primer número
    :param b: segundo número
    :return: multiplicación de a y b
    """
    return a * b
def division(a, b):
    """
    Divide dos números
    :param a: primer número
    :param b: segundo número
    :return: división de a y b
    """
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b
def potencia(a, b):
    """
    Eleva un número a la potencia de otro
    :param a: base
    :param b: exponente
    :return: a elevado a la potencia de b
    """
    return a ** b
def raiz_cuadrada(a):
    """
    Calcula la raíz cuadrada de un número
    :param a: número
    :return: raíz cuadrada de a
    """
    if a < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    return a ** 0.5