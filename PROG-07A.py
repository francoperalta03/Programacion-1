#3PROG-03A
#Integrantes: PERALTA, FRANCO / SOSA, TOMAS / NICOLAS SCHOEPF

#PEDIDO DE DATOS
print("Cuanto sale el producto?")

valorDelProducto = int(input())

print("Con cuanto vas a pagar?")
billete = int(input())

while valorDelProducto > 0: 
    if  billete < valorDelProducto:
        dineroInsuficente = valorDelProducto - billete 
        print("Tu dinero es insuficiente, tenes una deuda de " + str(dineroInsuficente) +" pesos")
        print("Con cuanto vas a pagar?")
        billete = int(input())
    else:
        vuelto = billete - valorDelProducto
        print ("Muchas gracias, tu vuelto es de " + str(vuelto) + " pesos")
        print("Cuanto sale el producto?")
        valorDelProducto = int(input())
        if valorDelProducto > 0:
            print("Con cuanto vas a pagar?")
            billete = int(input())

print ("GRACIAS VUELVA PRONTO")

