

# juego en el que la maquina gener un num aleatori del 1.100
# el jugador intente adivinar hasta q lo consigue
#la maquina da pistas ( mas alto o mas lejos)

import random as r

numeroGenerado = (r.randint(1,20))

numero = False
while not numero :
    intento = int(input("Introduzca un numero del 1 al 20: "))

    if intento == numeroGenerado:
        print("El numero es correcto 🤞🤞🤞🤞")
        numero = True

    elif intento > numeroGenerado:
        print("El numero es incorrecto, es mayor que el numero que buscas")

    else:
        print("El numero es incorrecto, es menor que el numero que buscas")


