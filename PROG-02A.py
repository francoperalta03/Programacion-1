#3PROG-02A
#Integrantes: PERALTA, FRANCO / SOSA, TOMAS

#OBTENCION DE DATOS
cantCombustible = int (input("¿Cual es la cantidad de combustible que posee?"))

#CALCULO Y RESULTADO
if cantCombustible < 5:
    print("Debe cargar nafta!")
else:
    print("Usted puede recorrer:", cantCombustible * 14.1, "km")
