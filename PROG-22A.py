# PROG-22A
# Version 1.0
# Programa de devolver nombre invertido
# Autores: Matteozzi, Marzorati, Sosa, Peralta

# Variable para almacenar el nombre invertido
nombreInvertido = ""
# Obtener info
nombre = str(input("Ingresar el nombre que desea invertir: "))
# Guardar letras al reves
for i in range(len(nombre)-1, -1, -1):
    nombreInvertido = nombreInvertido + nombre[i]
# Imprimir el resultado
print(f" El nombre invertido es {nombreInvertido}.")