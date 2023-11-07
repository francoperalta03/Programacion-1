# PROG-31A
# Version 1.0
# Programa para ingresar nombres y guardar en una lista
# Autores: Sosa, Peralta

# Lista de nombres
listaNombres = []
# Contador
alumnos = 0
# Mensaje bienvenida
print("¡Bienvenido al numerador de alumnos! ¡Para terminar el programa debe escribir FIN!")
# Ingresar nombres y almacenar en lista hasta que se escriba FIN
while True:
    alumnos = alumnos + 1
    nombreAlumno = input(f"Ingrese el nombre del alumno {alumnos}: ")
    if nombreAlumno == "FIN":
        break
    listaNombres.append(nombreAlumno)
# Ordenar e imprimir nombres
listaNombres.sort()
print("\n"
      "Los alumnos son: \n"
      "---------------")
for i in range(0, len(listaNombres), 1):
    nombre = str(listaNombres[i])
    print(f"{i+1:02}...{nombre.capitalize()}")
# Vaciar contador
alumnos = 0
    