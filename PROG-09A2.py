#PROG-09A
#INTEGRANTES SOSA TOMAS ANTONIO BRKUSIC / FRANCO PERALTA


print("Cual es el precio base del producto?")
precioProducto = int(input())

print("Como vas a pagar? 0 para efectivo // tarjeta insertar 1,3,6,12 cuotas")
cuotas = int(input())

if cuotas == 0:
    precioEfectivo = precioProducto / 1.10
    print("el valor del producto abonando en efectivo es de", str(precioEfectivo), " pesos")
elif cuotas == 1:
    tipoCuota1 = precioProducto * 1
    print ("el valor en 1 cuota es de ", str(tipoCuota1)," pesos")
elif cuotas == 3:
    tipoCuota2 = (precioProducto * 1.05)/3
    print("el valor en 3 cuotas es de ", str(tipoCuota2), " pesos")
elif cuotas == 6: 
    tipoCuota3 = (precioProducto * 1.10)/6
    print ("el valor en 6 cuotas es de ", str(tipoCuota3)," pesos")
elif cuotas == 12: 
    tipoCuota4 = (precioProducto * 1.15)/12
    print ("el valor del producto en 12 cuotas es de ", str(tipoCuota4), " pesos")
else: 
    print("cuota invalida")