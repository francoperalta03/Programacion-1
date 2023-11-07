# PROG-27A
# Version 1.0

#autores: Peralta, Sosa

# Abrir lista
materiasLista = []
# Obtener datos
cantMaterias = int(input("¿Cuantas materias estás cursando?\n"))
for i in range(1, cantMaterias + 1, 1):
    materia = str(input(f"Escribir el nombre de la materia {i}:\n"))
    materiasLista.append(materia)
# Imprimir resultado
print("Las materias son:", materiasLista)
