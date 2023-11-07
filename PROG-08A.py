contador = 0
notasAlumnos = 0

print ("cuantos alumnos rindieron el examen?")
alumnos = int(input())


if alumnos > 0: 
    for i in range(1, alumnos + 1, 1): 
        contador = contador + 1
        print("cual es la nota del alumno?", contador)
        nota = int(input())
        notasAlumnos= notasAlumnos + nota
        promedioNotas= notasAlumnos / contador   
       
        
    print ("el promedio de notas del curso es de: ", promedioNotas)
else: 
    print ("ningun alumno rindio el examen")
 

        
    
    

