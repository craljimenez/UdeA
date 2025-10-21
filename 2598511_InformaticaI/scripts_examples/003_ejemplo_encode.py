mensaje = input("Ingrese mensaje: ")
vocales = "aeiou"
word = ""
new_encoded = ""

mensaje += " "

for char in mensaje:
    if char != " ":
        word += char
    else:
        par = ""
        impar = ""
        i = 0
        for l in word:
            if l in vocales:
                k = 0
                while k < len(vocales):
                    if l == vocales[k]:
                        l = str(k + 1)
                        break
                    k += 1
            if i%2 == 0: # Index par
                par += l
            else: # index impar
                impar += l
            i += 1
        new_word = par+impar # concatenar
        word = ""
        new_encoded += new_word + " "

new_encoded = new_encoded[:-1]
print(new_encoded)
a = 1