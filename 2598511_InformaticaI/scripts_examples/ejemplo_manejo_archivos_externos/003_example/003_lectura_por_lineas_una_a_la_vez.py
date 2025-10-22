file = open("./texto.txt",mode="r")

i = 1
for linea in file:
    print("linea ",i," :'",linea,"'",sep="")
    i += 1



file.close()