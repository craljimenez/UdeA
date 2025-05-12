contador = 5 # variable Global
def externa():
    contador = 0 # Variable Local
    print("Dentro de externa, antes de interna,contador =", contador)

    def interna():
        nonlocal contador # VAriable Local de la función externa
        contador = 50
        contador += 1 # contador = contador + 1
        print("Dentro de interna, contador =", contador)

    interna()
    print("Dentro de externa, contador =", contador)

print("Antes de función, contador",contador)
externa()
print("Después de función, contador",contador)
