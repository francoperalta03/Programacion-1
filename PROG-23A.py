# PROG-23A
# Version 1.0
# Programa para poner en mayuscula todas las vocales de una frase
# Autores: Matteozzi, Marzorati, Sosa, Peralta

# Variable para almacenar el string final
fraseConVocalesMayus = ""
# Obtener frase
frase = str(input("Ingresar la frase que desea transformar con vocales mayúsculas: "))
# Agregar todos los caracteres al otro string y si son vocales agregarlos en mayusculas
for i in range(0, len(frase), 1):
    if frase[i] == "a" or frase[i] == "e" or frase[i] == "i" or frase[i] == "o" or frase[i] == "u":
        fraseConVocalesMayus = fraseConVocalesMayus + str.upper(frase[i])
    else:
        fraseConVocalesMayus = fraseConVocalesMayus + frase[i]
# Imprimir resultados
print("La frase final es:  " + fraseConVocalesMayus)