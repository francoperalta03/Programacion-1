#loteria 
# Autores : PERALTA
 
import random
memoria = ""
seguir = 1

while seguir == 1:
    
    while True: 
        bolilla = str(random.randint (1, 90))
        if memoria.find(" " + bolilla + " ") == -1:
            break 
    input()
    memoria = memoria + " " + bolilla + " "
    print("CANTAR --- " + bolilla + " ---")
    print ()
    print("YA CANTADOS:" + memoria)
    print()

  