#PROG-15A
#Integrantes: PERALTA, FRANCO / SOSA, TOMAS

print ("cuantos alumnos son")
alumnos =int (input())

if alumnos >= 100:
    monto1= alumnos * 120000
    print ("cada alumno pagaria 120000 pesos, el total a pagar por", alumnos, "alumnos, es de", monto1, "pesos")
    
elif alumnos > 50 and alumnos < 99:
    monto2= alumnos * 135000
    print ("cada alumno pagaria 135000 pesos, el total a pagar por", alumnos, "alumnos, es de", monto2, "pesos")
    
elif alumnos > 30 and alumnos < 49:
    monto3 = alumnos * 150000
    print ("cada alumno pagaria 150000 pesos, el total a pagar por", alumnos, "alumnos, es de", monto3, "pesos")

else: 
    monto4 = 4500000 / alumnos
    print ("con un total de 4.500.000 millones por el grupo de", alumnos, "alumnos, el monto a pagar por alumno es de", monto4, "pesos")
    
    
