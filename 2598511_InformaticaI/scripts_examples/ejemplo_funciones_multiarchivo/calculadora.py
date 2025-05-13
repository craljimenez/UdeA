#%% Funciones
"""
import crea un objeto, y las funciones del archivo son metodos de este.
"""
# import operaciones
import operaciones as alias_op # alias_op.suma(a,b), alias_op.resta(a,b) , etc. 
"""
from trae la función tal cual se tiene definida.
"""
from operaciones import suma,\
                        resta,\
                        multiplicacion,\
                        division,\
                        potencia,\
                        raiz_cuadrada
# from operaciones import * # uso de comodín * para llamar todas las funciones generadas en operaciones.py


print("""
Opción\t Operación
a\t sumar
b\t restar
c\t multiplicar
d\t dividir
e\t potencia
f\t raiz_cuadrada
      """)

op = input("Ingresé Opción:")
op = op.lower() # Con método de la cadena

a = float(input("Ingrese valor:"))
if op != "f":
    b = float(input("Ingrese valor:"))

if op == 'a':
    print(f"Suma de {a}+{b} =", suma(a,b))
elif op == "b":
    print(f"Resta de {a}-{b} =", resta(a,b))
elif op == "c":
    print(f"Multiplicaciíon de {a}*{b} =", multiplicacion(a,b))
elif op == "d":
    print(f"División de {a}/{b} =", division(a,b))
elif op == "e":
    print(f"Potebcia de {a}^{b} =", potencia(a,b))
elif op == "f":
    print(f"Raiz Cuadrada de {a} =", raiz_cuadrada(a))
else:
    raise ValueError(f"La opción ingresada: {op} no es válida.\
Ingrese 'a', 'b', 'c', 'd', 'e' o 'f'.")



# %%
