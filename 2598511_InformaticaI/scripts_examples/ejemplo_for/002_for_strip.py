"""
Script recibe mensaje de texto del usuario
y retorna el mensaje ingresado sin espacios
al inicio y al final
"""
# Se lee el mensaje ingresado por el usuario
mensaje = input("Ingrese mensaje:")
# int() o float()

# Quitando los primeros espacios
# las strings en python son Inmutables. No se puede cambiar ningun valor de la misma.
# Se concatena string por medio de +. string1 + string2 (genera la concatenación de las dos string)

#%% Quitando Espacios de la Izquierda

new_mensaje = ""
son_primeros_espacios = True
for char in mensaje:
    if son_primeros_espacios:
        if char != " ":
            son_primeros_espacios = False
            new_mensaje = new_mensaje + char
    else:
        new_mensaje = new_mensaje + char


#%% Quitando Espacios de la Derecha

mensaje_salida = ""
mensaje_reversa = new_mensaje[::-1] # Revierte el orden de la cadena, a = "Hola" entonces a_reverse = "aloH"

son_primeros_espacios = True
for char in mensaje_reversa:
    if son_primeros_espacios:
        if char != " ":
            son_primeros_espacios = False
            mensaje_salida = mensaje_salida + char
    else:
        mensaje_salida = mensaje_salida + char

mensaje_salida = mensaje_salida[::-1]

print(mensaje_salida,"|",sep="")