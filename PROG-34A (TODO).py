# PROG-31A
# Version 1.0
# Programa para mostrar las lineas de trenes
# Autores: Sosa, Peralta
# Funciones
def imprimirLinea(linea):
    for i in range(0, len(linea), 1):
        print(f"    •{linea[i]}")
    print("\n")

# Listas
lineaSanMartin = ["Formación 011", "Formación 012", "Formación 013", "Formación 014"]
lineaUrquiza = ["Formación 017", "Formación 002", "Formación 015", "Formación 014", "Formación 001", "Formación 004", "Formación 005"]
lineaMitreA = ["Formación 018", "Formación 028", "Formación 058", "Formación 048", "Formación 089", "Formación 009", "Formación 005"]
lineaMitreB = ["Formación 018", "Formación 028","Formación 058", "Formación 048", "Formación 089"]
trenesEnVariasLineas = []

# Imprimir lineas
# San Martín
print("Línea San Martín")
imprimirLinea(lineaSanMartin)
# Urquiza
print("Línea Urquiza")
imprimirLinea(lineaUrquiza)
# Mitre A
print("Línea Mitre A")
imprimirLinea(lineaMitreA)
# Mitre B
print("Línea Mitre B")
imprimirLinea(lineaMitreB)

# Ver si se repiten lineas
TODO
