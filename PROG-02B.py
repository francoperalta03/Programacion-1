#3PROG-02b
#Integrantes: PERALTA, FRANCO / SOSA, TOMAS

#OBTENCION DE DATOS
print()
print("cuantos litros de nafta posee?")
litros = int(input())

print("ingrese tipo de camino. [c=CIUDAD; r=RUTA]")
camino = input()

#CALCULO
if camino == "r":
    kmRecorridos = int(litros) * 14.1
else:
	kmRecorridos = int(litros) * 10.3
    
#RESULTADO
print()
print("Con", litros, "litros de nafta, podes recorrer", kmRecorridos, "km")

