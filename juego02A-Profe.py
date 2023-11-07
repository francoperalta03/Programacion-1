"""
-----------------------------------------------------------------------------------------------
Programa juego de lotería ¡Bingo!
Simula la extracción no repetida de bolillas de bingo (valores del 1 al 90)
Pendiente:
    Falta mejorar el código para que el programa termine cuando se extrajeron todas las bolillas
-----------------------------------------------------------------------------------------------
"""

# IMPORTACIÓN DE MÓDULOS
import random   # Necesario para generar los números aleatorios del bolillero

# DECLARACIÓN DE FUNCIONES
"""
Función para determinar si un valor de bolilla ya fue cantado en extracciones anteriores.
PARÁMETROS:
    bol: string con el valor de bolilla que se quiere revisar si salió previamente.
    mem: string conteniendo todos los valores de bolilla que salieron previamente.
SALIDA:
    True: si bol está dentro de mem, es decir si ya salió la bolilla.
    False: si bol no está dentro de mem, es decir si la bolilla aún no salió.
"""
def yaCantado(bol, mem):
    posicion = mem.rfind(" " + bol + " ")  # Busca bol dentro de mem, devuelve -1 si no lo encuentra
    if posicion == -1:  # Si no encuentra bol dentro de mem ...
        return False    # ... la bolilla no fue cantada
    else:               # Si encuentra bol dentro de mem ...
        return True     # ... la bolilla ya fue cantada

# PROGRAMA PRINCIPAL
memoria = ""    # Variable para almacenar los valores de bolilla que van saliendo.
print()
input("Presione ENTER para sacar la primera bolilla.")

while True: # Este bucle se repite por cada extracción de bolilla
    while True: # Este bucle se repite hasta que se obtiene una bolilla que no haya salido
        bolilla = str(random.randint(1, 90))        # Se genera un valor de bolilla de 1 a 90 y se lo covierte a string
        if yaCantado(bolilla, memoria) == False:    # Sólo sale del bucle si se obtiene un valor de bolilla que no haya salido
            break
    print()
    print("¡CANTAR! >>>>> " + bolilla + " <<<<<")
    memoria = memoria + " " + bolilla + " "         # Se almacena el valor cantado. El patrón de almacenamiento es espacio+valor+espacio
    print("Ya cantados: ", memoria)
    print()
    input("Presione ENTER para sacar otra bolilla.")

