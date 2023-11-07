# PROG-21A
# Version 1.0
# Programa para abreviar los meses
# Autores: Matteozzi, Marzorati, Sosa, Peralta

# Obtener mes
mes = str(input("Ingrese el nombre del mes que desea abreviar: "))
# Acortar string
mesAbreviado = mes[0:3]
# Imprimir resultado
print(f"La abreviación del mes es {str.upper(mesAbreviado)}.")