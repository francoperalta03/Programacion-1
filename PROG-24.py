#PROG-24
#AUTORES: PERALTA FRANCO, SOSA TOMAS ANTONIO BRUKSIC
#VERSION: 1.0

# Funcion de validacion
def validacion(contraseña):
    #si la contraseña es menor a 8 caracteres, no es valida
    if(len(contraseña) < 8):
        print("contraseña invalida no tiene 8 caracteres")
        return False
    # Contraseña debe de tener al menos 2 numeros
    numeros = 0
    for i in range (0,len(contraseña),1):
        if(contraseña[i].isnumeric()):
            numeros = numeros + 1
    if numeros < 2:
        print("contraseña invalida, no posee 2 caracteres numericos como minimo")
        return False
    # Contraseña debe de tener al menos 1 mayus
    mayus = 0
    for i in range (0,len(contraseña),1):
        if(contraseña[i].isupper()):
            mayus = mayus + 1
    if mayus < 1:
        print("contraseña invalida, no posee mayusculas")
        return False
     # Contraseña debe de tener al menos 1 minus
    minus = 0
    for i in range (0,len(contraseña),1):
        if(contraseña[i].islower()):
            minus = minus + 1
    if minus < 1:
        print("contraseña invalida, no posee minus")
        return False
     # Si pasa todos los chequeos es verdadero
    return True

# Inicializar el programa en falso
validarContraseña = False
#obtencion de datos
while validarContraseña == False:
    contraseñaIngresada = input("ingrese contraseña:  ") 
    validarContraseña = validacion(contraseñaIngresada)
# Si es verdadero decir q es valida
print("La contraseña es valida! es supercalifrasticoespialidoso")


