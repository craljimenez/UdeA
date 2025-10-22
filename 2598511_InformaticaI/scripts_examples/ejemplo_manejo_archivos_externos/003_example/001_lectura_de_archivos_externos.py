file = open("./texto.txt",mode="r")

string_file = file.read(100) # Leyendo los primeros 100 caracteres de documento. 
string_file2 = file.read()

print("len(string_file):",len(string_file))

print("string_file:",string_file)

print("string_file2:",string_file2)


file.close()