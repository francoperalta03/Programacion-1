# PROG-05A

# Autor: franco peralta / tomas sosa

# Obtener datos
tipoTarjeta = int(input("¿Que tipo de tarjeta posee? "))
limiteTarjeta = int(input("¿Cual es el limite? "))

# Si el tipo de tarjeta es 1, aumentar el limite un 25%
if tipoTarjeta == 1:
    print("¡Su nuevo limite es de: $", limiteTarjeta * 1.25)
    
# Si el tipo de tarjeta es 2, aumentar el limite un 35%
elif tipoTarjeta == 2:
    print("¡Su nuevo limite es de: $", limiteTarjeta * 1.35)
    
# Si el tipo de tarjeta es 3, aumentar el limite un 45%
elif tipoTarjeta == 3:
    print("¡Su nuevo limite es de: $", limiteTarjeta * 1.45)
    
# Si el tipo de tarjeta es otro, aumentar el limite un 50%
else:
    print("¡Su nuevo limite es de: $", limiteTarjeta * 1.50)