
valoresMonedas = [2,1,0.50,0.20,0.10,0.05]
reservaMonedas = [20,20,20,20,20,20]
nombreProductos=["agua","refresco","Jugo"]
precioProductos=[0.50,0.75,0.95]

def printMenu(nombres,precios):
    if len(nombres) != len(nombres):
        return False
    textoMenu = "Hola ¿que desea?\n"
    for i in range(len(nombres)):
        textoMenu += f"{i+1}. {nombres[i]} : {precios[i]}\n"
    textoMenu += f"{len(nombres) + i} - Salir"
    print(textoMenu)

def elegirProducto(producto):
    opcion = input("Elija una opcion => ")
    numeroProductos = []
    for i in range (len(producto)):
        numeroProductos.append(str(i+1))

    while opcion not in numeroProductos:
        opcion = input("Elija una opcion valida => ")
    return int(opcion)-1


def ingresarImporte(opcion):
    precio = precioProductos[opcion]
    importeUsuario =  0
    monedasIntroducidas = []

    while importeUsuario < precio:
        print(f"Te falta introducir {round(precio-importeUsuario,2)}.")
        moneda = ingresarMoneda()
        importeUsuario += moneda
        monedasIntroducidas.append(moneda)
   # if importeUsuario > precio:
    #    resto = importeUsuario - precio
     #   darCambio(resto)

        entregarProducto(nombreProductos[opcion])
        sumarMonedas(monedasIntroducidas)



def entregarProducto(nombre):
    print(f"Aqui va su {nombre}")



def sumarMonedas(monedas):
    for moneda in monedas:
        reservaMonedas[valoresMonedas.index(moneda)] += 1


def ingresarMoneda():
    valoresValidos = []
    for valor in valoresMonedas:
        valoresValidos.append(str(valor))
    moneda = input("Ingrese una moneda: ")
    while moneda not in valoresValidos:
        moneda = input("Ingrese una moneda correcta: ")
    return float (moneda)

printMenu(nombreProductos, precioProductos)
opcion = elegirProducto(nombreProductos)

if opcion == len(nombreProductos)+1:
    print("gracias por la compra")
else:
    ingresarImporte(opcion)
    print(valoresMonedas)
    print(reservaMonedas)