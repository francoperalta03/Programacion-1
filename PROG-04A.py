#3PROG-04A
#Integrantes: PERALTA, FRANCO / SOSA, TOMAS

#pedido da datos
print("cuantos inscriptos hay en la conferencia?")
inscriptos = input ()
print("cuantos asientos hay en el auditorio?")
asientos = input ()

#calculo
(asientosInsuficientes)= int(inscriptos) - int(asientos)
   
#resultado
if inscriptos > asientos:
 
    print("la cantidad de asientos es insuficiente, faltan ", (asientosInsuficientes), "asientos")

else:
    print ("la cantidad de asientos es suficiente")
50