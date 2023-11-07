# PROG-30A
# Version 1.0
# Programa para escribir el número de mes y que devuelva el mes escrito
# Autores: Sosa, Peralta
# Funcion
def conversionMes(n):
    if n <= 12 and n > 0:
        nM = Meses[n-1]
        return nM
    else:
        print("¡Ingrese un número de mes valido!")
# Lista de meses
Meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
# Obtener número de mes
numeroMes = int(input("Ingresar el número del mes que desea saber:\n"))
nombreMes = conversionMes(numeroMes)
# Imprimir resultado
print(f"El nombre del mes {numeroMes} es {nombreMes}.")

