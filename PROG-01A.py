#PROG-1A

#Integrantes: PERALTA, FRANCO / SOSA, TOMAS

#OBTENCION DE DATOS
print("cual es el valor del producto?")
precio = input()
print("cuantas unidades compro?")
unidades = input()

#CALCULOS
(precioBruto) = int(precio) * int(unidades)
(descuento) = precioBruto * float(0.2)
(precioConDescuecuento) = precioBruto - descuento
(precioFinal) = precioConDescuecuento * float(1.21)
(precioIva)= precioConDescuecuento * float (0.21)

#RESULTADO
print( "el valor con descuento es de...")
print(precioConDescuecuento)
print("el valor del iva es de...")
print(precioIva)
print("el valor a pagar con IVA incluido es de...")
print(precioFinal)
