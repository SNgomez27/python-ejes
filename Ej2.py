#Realizar un programa que pida u nnuemro emtero positivo de n cifrsa y que compruebe
# si el nuemor es capicua

numero = input("ingresa un numero:")

esCapicua = True

for i in range(len(numero)//2):
    if numero[i] != numero[-1 -i]:
        esCapicua = False

    if esCapicua:
        print("es capicua")
    else:
        print("no es capicua")