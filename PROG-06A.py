# PROG-06A

# Autor: Tomás Sosa / Peralta Franco

repetir = 1
while repetir == 1:
    # Obtener datos
    precioProducto = float(input("¿Cual es el valor del producto que desea adquirir? "))
    # Si el precio es 0 cortar el while
    if precioProducto == 0:
        break
    cantidadDinero = float(input("¿Cuanto dinero posee? "))
    # Si la cantidad de dinero es menor al precio del producto no le va a alcanzar el dinero
    if cantidadDinero < precioProducto:
        print("¡Usted no posee el dinero necesario para poder comprar el producto!")
    # Sino calcular y devolver el vuelto
    else:
        # Calcular e imprimir el vuelto
        print("Su vuelto seria:", cantidadDinero - precioProducto,".")
    # Preguntar si desea comprar más productos
    repetir = int(input("desea cargar mas productos? [si: 1 / no : 0]"))
# Mensaje despedida
print("Gracias por su compra")