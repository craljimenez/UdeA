def contar_vocales(cadena_texto):
    vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    contador_vocales = 0
    num_vocales = len(vocales)
    N = len(cadena_texto)
    # i,j = 0,0
    i = 0
    while i < N:
        j = 0
        while j < num_vocales:
            if cadena_texto[i] == vocales[j]:
                contador_vocales += 1
            j += 1
            
        i += 1
            
    return contador_vocales

print(contar_vocales("aeiou"))
