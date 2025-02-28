import os

ruta = ".."
for fichero in os.listdir(ruta):
    rutaFichero = os.path.join(ruta, fichero)
    if os.path.isdir(rutaFichero):
        print(f"{fichero} es un directorio")
    elif os.path.isfile(rutaFichero):
        print(f"{fichero} es un archivo")
    else:
        print("desconocido")