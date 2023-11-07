# PROG-32A
# Version 1.0
# Programa para ingresar nombres y guardar en una lista
# Autor: Matteozzi, Marzorati, Santos, Sosa, Peralta

# Importar librerias
import random
# Funcion para generar listas random
def listaDeItems():
    alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    lista = []
    largoLista = random.randint(5, 10)
    for x in range(0, largoLista):
        lista.append(random.choice(alfabeto))
    return lista
# Listas
listaGenerada1 = listaDeItems()
listaGenerada2 = listaDeItems()
listaGenerada3 = []
# Chequear si los elementos pertenecientes a lista 1 se encuentran en la 2 y si están agregar a la 3
for i in range(0, len(listaGenerada1),1):
    if listaGenerada1[i] in listaGenerada2:
        listaGenerada3.append(listaGenerada1[i])
# Imprimir resultados
print("La lista 1 es: \n"
      f"{listaGenerada1} \n")
print("La lista 2 es: \n"
      f"{listaGenerada2} \n")
print("Los elementos en común son: \n"
      f"{listaGenerada3} \n")

