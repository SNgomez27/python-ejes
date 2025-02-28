import random
from BlackJackCarpet.Carta import Carta

# Definimos los palos y los valores (representados como string)
PALOS = ['♥', '♦', '♣', '♠']
VALORES = ['A'] + [str(n) for n in range(2, 11)] + ['J', 'Q', 'K']


def crear_mazo():
    # Se crea un mazo de objetos Carta con su palo, valor numérico y nombre (por ejemplo, "A♥")
    mazo = []
    for palo in PALOS:
        for valor in VALORES:
            nombre = f"{valor}{palo}"
            # Determinamos el valor numérico: para las figuras es 10, para el As inicialmente 11, y para el resto se convierte a int.
            if valor in ['J', 'Q', 'K']:
                valor_numerico = 10
            elif valor == 'A':
                valor_numerico = 11
            else:
                valor_numerico = int(valor)
            mazo.append(Carta(palo, valor_numerico, nombre))
    random.shuffle(mazo)
    return mazo


def calcular_valor(mano):
    total = 0
    aces = 0
    for carta in mano:
        # Si el nombre de la carta comienza con 'A', es un As
        if carta.nombre.startswith('A'):
            total += 11
            aces += 1
        else:
            total += carta.valor
    # Si el total supera 21, convertimos cada As de 11 a 1 (restando 10)
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total


def mostrar_mano(mano):
    # Se utiliza el método __str__ de la clase Carta para mostrar cada carta (por ejemplo, "A♥")
    return ', '.join(str(carta) for carta in mano)


def juego():
    mazo = crear_mazo()
    # Se reparten dos cartas para el jugador y dos para la casa
    jugador = [mazo.pop(), mazo.pop()]
    casa = [mazo.pop(), mazo.pop()]

    print("Tus cartas:", mostrar_mano(jugador), "| Valor:", calcular_valor(jugador))
    print("Carta visible de la casa:", str(casa[0]))

    # Turno del jugador
    while calcular_valor(jugador) < 21:
        decision = input("¿Pedir o plantarse? ").lower()
        if decision == 'pedir':
            jugador.append(mazo.pop())
            print("Tus cartas:", mostrar_mano(jugador), "| Valor:", calcular_valor(jugador))
        elif decision == 'plantarse':
            break
        else:
            print("Elige 'pedir' o 'plantarse'.")

    if calcular_valor(jugador) > 21:
        print("Te pasaste. ¡Perdiste!")
        return

    # Turno de la casa: la casa pide cartas hasta alcanzar un valor de 17 o más
    print("\nTurno de la casa.")
    while calcular_valor(casa) < 17:
        casa.append(mazo.pop())
        print("Cartas de la casa:", mostrar_mano(casa), "| Valor:", calcular_valor(casa))

    valor_jugador = calcular_valor(jugador)
    valor_casa = calcular_valor(casa)
    print("\nValor final del jugador:", valor_jugador)
    print("Valor final de la casa:", valor_casa)

    if valor_casa > 21 or valor_jugador > valor_casa:
        print("¡Ganaste!")
    elif valor_jugador == valor_casa:
        print("Empate, gana la casa.")
    else:
        print("La casa gana.")


if __name__ == '__main__':
    while True:
        juego()
        if input("\n¿Deseas jugar de nuevo? (s/n): ").lower() != 's':
            print("¡Gracias por jugar!")
            break
