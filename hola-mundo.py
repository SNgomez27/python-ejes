print("hola mundo"*5)

str()
int()
float()
variable=4
otravariable = "saludo2"
numero =int(input("mete un cosa"))
print(len(otravariable))

lista = [1,2,3,4,otravariable,6,7,"goku pelado",9,123455]
print(lista)

2==2
2!=2
2<=2
2<2
1==1 and 3== 2
not(2!=2 or 1==1)

print("a" in "aeiou")

print("s" not in "aeiou")

if "e" not in "aeiou":
    print("no ta")
else:
    print("ta")



    esCierto = False
    while not esCierto:
        print("eeee")
        esCierto = True


for i in range(10):
    print(i)


def tieneA(nombre):
    if "a" in nombre.lower():
        return True
    return False


lista=["SOL", "BO", "JUAN", "JOSE", "CAMI", "KAILE"]
for i in range(len(lista)-1,0,-1):
    print(lista[i])

    for alumno in lista:
        if tieneA(alumno):
            print(f"{alumno.capitalize()} contienen la letra a ")