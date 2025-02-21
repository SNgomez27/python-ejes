from matrices.matrices_utils import printMatrix

tabla = []

for i in range(10):
    tabla.append([])
    for j in range(10):
        if i % 2 == 0:
            tabla[i].append("1")
        else:
            tabla[i].append("0")




printMatrix(tabla)