"""5. crear un diccionario y trabajar con sus valores"""
import json

dicionarioAnidados = {
    "Maokai":{"top"},
    "jinx":{"adc"},
    "lux":{
        1:"mid",
        2:"sup"}
}

diccionarioConListas = {
    "maokai" : ["champ de lol muy bueno que se juega support o top"],
        "adc":["jinx,ezreal",],
}


palabraNuev = input("escribi una palabra nuevo o si desea salir 'exit'\n")
while palabraNuev != "exit":
    definicion = input("escribi a definion:\n")
    diccionarioConListas[palabraNuev] = [definicion]
    palabraNuev = input("escribi una palabra nuevo o si desea salir 'exit'\n")

with open("diccionario","w", encoding="utf-8") as file:
    json.dump(diccionarioConListas,file,indent=4)

print(dicionarioAnidados["lux"][1])

busqueda = input("Ingresa tu busqueda: ")
if busqueda in diccionarioConListas:
    cont = 1
    for acepcion in diccionarioConListas[busqueda]:
      print(f"{cont}. {acepcion}")
      cont += 1
else:
    print("No existe la busqueda")