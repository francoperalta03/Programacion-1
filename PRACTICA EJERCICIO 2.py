dias= 0
temperaturaSemanal= 0
print ("bienvenido")


    
while temperaturaSemanal < 7:
   
    temperaturaDiaria= float(input("cual es la temperatura diaria? "))
    if temperaturaDiaria < -25 or temperaturaDiaria > 45: 
        print ("no es una temperatura valida, ingrese otra temperatura")
        continue
    temperaturaSemanal =temperaturaSemanal +1
    dias=dias + temperaturaDiaria
    
        
temperaturaPromedio= dias / 7

print ("el promedio de temperatura en la semana es de", temperaturaPromedio)




