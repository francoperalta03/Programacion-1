# PROG-37A
# Version 1.0
# Programa para realizar 6 opciones respecto al estacionamiento de colectivos
# Autor: Matteozzi

# Mensaje inicio
opcionSeleccionada = int(input("SELECCIONAR UNA DE LAS 6 OPCIONES\n"
                               "1 - Registrar cada unidad cuando llega a la noche para su estacionamiento\n"
                               "2 - Registrar cada chofer a medida que se presenta a la mañana a trabajar\n"
                               "3 - Registrar y emitir un listado donde se le asigne a cada chofer presente y por orden de llegada la unidad más conveniente para salir\n"
                               "4 - Emitir un listado diario completo con la asignación de unidades por chofer donde aparezca “hora”, “nombre de chofer” y “número de unidad”\n"
                               "5 - Vaciar el registro anterior, para ejecutarlo por la mañana antes de que arribe el primer chofer\n"
                               "0 - Salir del programa"))
# Opcion 0
if opcionSeleccionada == 0:
    exit()
