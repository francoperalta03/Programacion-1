# PROG-25A
# Version 1.0
# Programa para ver si frase es alfabetica
# Autores: Matteozzi, Marzorati, Sosa, Peralta

# Funcion para validar
def validacion(palabra):
    alfabetica = True
    for i in range(1, len(palabra)+1,1):
        if i-1 > 0:
            if palabra[i-1] > palabra[i-2]:
                alfabetica = True
            else:
                alfabetica = False
                break
    return alfabetica

# Obtener datos
palabra = str(input("Ingresar una palabra: "))
# Validar si es alfabetica
validacionPalabra = validacion(palabra)
# Calculos
if validacionPalabra == True:
    print(f"La palabra {palabra} es alfabetica")
else:
    print(f"La palabra {palabra} NO es alfabetica")
    
