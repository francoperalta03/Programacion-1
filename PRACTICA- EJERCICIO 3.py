print ("bienvenido! que operacion desea realizar? ingresa [S] suma, [R] resta, [M] multiplicación o [D] división ")
operacion= str(input())
print ("ingrese 2 numeros para realizar la" + operacion )
x= int(input())
y= int(input())

if operacion == "S":
    s = x + y
    print("el resultado de la suma es de ", s)
elif operacion == "R":
    r = x - y
    print("el resultado de la resta es de", r)
elif operacion == "M":
    m = x * y
    print("el resultado de la multiplicacion es de", m)
elif operacion == "D": 
    while y == 0:
        print("NO SE PUEDE DIVIDIR POR 0 QULIAO")
        y = int(input("quliao"))    
    d = x / y
    print("el resultado de la division es de", d)
else:
    print("ingrese una operacion indicada QULIAO ")


 
