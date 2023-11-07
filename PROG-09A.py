
#
#PROG-09A
#Integrantes: PERALTA, FRANCO / SOSA, TOMAS / NICOLAS SCHOEPF


print("Cual es el precio base del producto?")
precioProducto = int(input())


print("Como vas a pagar? 1 para efectivo // 0 tarjeta")
tipodePago = int(input())

if tipodePago == 0:
    print ("cuantas cuotas lo vas a pagar? insertar 1,3,6,12")
    cuotas = int(input())
elif cuotas == 1: 
    tipoCuota1 = precioProducto * 1
    print ("el valor en 1 cuota es de ", tipoCuota1," pesos")
elif cuotas == 3:
tipoCuota2 = precioProducto * 1.05
print("el valor en 3 cuotas es de ", tipoCuota2, " pesos"
elif cuotas == 7:
    tipoCuota3 = precioProducto * 1.10
    print ("el valor en 3 cuotas es de ", tipoCuota3," pesos")
elif cuotas == 12: 
    tipoCuota4 = precioProducto * 1.15
    print ("el valor del producto en 12 cuotas es de ", tipoCuota4, " pesos")
else: 
    precioEfectivo = precioProducto / 1.10
    "el valor del producto abonando en efectivo es de", precioEfectivo, " pesos")
"""