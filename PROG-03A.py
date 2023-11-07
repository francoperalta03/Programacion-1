#3PROG-03A
#Integrantes: PERALTA, FRANCO / SOSA, TOMAS


#PEDIDO DE DATOS
print()
print ("cuanto sale el producto?")
valorDelProducto=int(input())

print("con cuanto vas a pagar?")
billete= int(input())

#CALCULO
dineroInsuficiente = valorDelProducto - billete
vuelto = billete - valorDelProducto


#RESPUESTA
if valorDelProducto > billete:
    print()
    print("tu dinero es insuficiente, te faltan...", dineroInsuficiente, ("pesos")) 

else:
    print()
    print ("muchas gracias por tu compra el vuelto es de", vuelto, ("pesos"))

    
    