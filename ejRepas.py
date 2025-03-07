#Realiza un ejercicio en python que pida al usuario un número entre el 5 y el 25 para determinar la longitud de una matriz cuadrada de nueva creación, que tendrá que rellenar con ceros, salvo la diagonal inversa en la que se irán poniendo los números de la serie de Fibonacci.

from matrices.matrices_utils import printMatrix

def validarEntrada(min, max):
    userInput = int(input("Introduzca un número del 5 al 25"))
    while userInput < 5 or userInput > 25:
        userInput = int(input("Introduzca un número correcto del 5 al 25"))
    return userInput

def fibonacci(longitud):
    listaFibonacci = []
    for i in range(longitud):
        if i < 2:
            listaFibonacci.append(i)
        else:
            listaFibonacci.append(listaFibonacci[i-1] + listaFibonacci[i-2])
    return listaFibonacci

matriz = []
longitud = validarEntrada(5,25)
lista = fibonacci(longitud)
for i in range(longitud):
    matriz.append([])
    for j in range(longitud):
        if j == longitud-1-i:
            matriz[i].append(lista[i])
        else:
            matriz[i].append(0)

printMatrix(matriz)