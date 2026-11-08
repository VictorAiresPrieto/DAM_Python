import random

def matrix_comparison(original_matrix,edited_matrix,mode):
    datos = ""
    final_fila = -1
    for fila in range(len(original_matrix)):
        for columna in range(len(original_matrix[fila])):
            datos = datos + str(original_matrix[fila][columna]).rjust(5)
        datos = datos + "|".rjust(4)

        if mode == "matrix to chain":
            inicio_fila = final_fila + 1
            final_fila = edited_matrix.find("\n",inicio_fila)
            datos = datos + edited_matrix[inicio_fila:final_fila]

        elif mode == "matrix to matrix":
            for columna in range(len(edited_matrix[fila])):
                datos = datos + str(edited_matrix[fila][columna]).rjust(5)
        datos = datos + "\n"
    return datos

#MATRIZ ALEATORIA:
dimension = 4
matriz = []
for fila in range(dimension):
    matriz.append([]) # mete una "casilla"
    #print("Fila =", fila)
    #print(matriz)
    for columna in range(dimension):
        #print("Columna =", columna)
        matriz[fila].append(random.randint(1, 100)) # mete el numero en la "casilla" que hemos "importado en el for fila in range
        #print(matriz)
datos = ""
for fila in range(dimension): # recorre la lista
    #print(lista[fila]) # imprime cada una de las filas
    for columna in range(dimension): # cada columna
        datos = datos + str(matriz[fila][columna]).rjust(5)
    datos = datos + "\n"
print(datos)
print("   -----------------")

#MATRIZ TRASPUESTA
datos = ""
for columna in range(dimension):
    #print(columna)
    for fila in range(dimension):
        #print(fila)
        datos = datos + str(matriz[fila][columna]).rjust(5)
    datos = datos + "\n"

print(matrix_comparison(matriz,datos,"matrix to chain"))

print("   -----------------")
#MATRIZ INVERTIDA COLUMNAS
datos = ""
for fila in range(dimension):
    #print(columna)
    for columna in range(dimension-1, -1, -1):
        #print(fila)
        datos = datos + str(matriz[fila][columna]).rjust(5)
    datos = datos + "\n"
print(matrix_comparison(matriz,datos, "matrix to chain"))

print("   -----------------")
#MATRIZ INVERTIDA FILAS
datos = ""
for fila in range(dimension-1, -1, -1):
    #print(columna)
    for columna in range(dimension):
        #print(fila)
        datos = datos + str(matriz[fila][columna]).rjust(5)
    datos = datos + "\n"
print(matrix_comparison(matriz,datos, "matrix to chain"))

print("   -----------------")
#MATRIZ SUMA DE TODOS LOS ELEMENTOS DE LA MISMA FILA
datos = ""
for fila in range(dimension):
    #print(columna)
    total_fila = 0
    for columna in range(dimension):
        total_fila = total_fila + matriz[fila][columna]
    for columna in range(dimension):
        #print(fila)
        datos = datos + str(total_fila-(matriz[fila][columna])).rjust(5)
    datos = datos + "\n"

#MATRIZ SUMA DE TODOS LOS ELEMENTOS DE LA MISMA FILA ALTER
lienzo = []
for l_fila in range(dimension):
    lienzo.append([])
    for l_columna in range(dimension):
        lienzo[l_fila].append(0)
        for columna in range(dimension):
            if l_columna != columna:
                lienzo[l_fila][l_columna] = lienzo[l_fila][l_columna] + matriz[l_fila][columna]
print(matrix_comparison(matriz,lienzo, "matrix to matrix"))

print("   -----------------")
#MATRIZ SUMA DE TODOS LOS ELEMENTOS DE LA MISMA COLUMNA
lienzo = []
for l_fila in range(dimension):
    lienzo.append([])
    for l_columna in range(dimension):
        lienzo[l_fila].append(0)
        for fila in range(dimension):
            if l_fila != fila:
                lienzo[l_fila][l_columna] = lienzo[l_fila][l_columna] + matriz[fila][l_columna]
print(matrix_comparison(matriz,lienzo, "matrix to matrix"))

#MATRIX SUMA DE TODOS LOS ELEMENTOS DE MISMA COLUMNA Y FILA
lienzo = []
for l_fila in range(dimension):
    lienzo.append([])
    for l_columna in range(dimension):
        lienzo[l_fila].append(0)
        for fila in range(dimension):
            if l_fila != fila:
                lienzo[l_fila][l_columna] = lienzo[l_fila][l_columna] + matriz[fila][l_columna]
        for columna in range(dimension):
            if l_columna != columna:
                lienzo[l_fila][l_columna] = lienzo[l_fila][l_columna] + matriz[l_fila][columna]
print(matrix_comparison(matriz,lienzo, "matrix to matrix"))

#MATRIX SOLO LA DIAGONAL
lienzo = []
for l_fila in range(dimension):
    lienzo.append([])
    for l_columna in range(dimension):
        lienzo[l_fila].append(0)
        if l_fila == l_columna:
            lienzo[l_fila][l_columna] = matriz[l_fila][l_columna]
print(matrix_comparison(matriz,lienzo, "matrix to matrix"))

#MATRIX SUMA SOLO LA DIAGONAL
lienzo = []
for l_fila in range(dimension):
    lienzo.append([])
    for l_columna in range(dimension):
        lienzo[l_fila].append(0)
        if l_fila == l_columna:
            for fila in range(dimension):
                if l_fila != fila:
                    lienzo[l_fila][l_columna] = lienzo[l_fila][l_columna] + matriz[fila][l_columna]
            for columna in range(dimension):
                if l_columna != columna:
                    lienzo[l_fila][l_columna] = lienzo[l_fila][l_columna] + matriz[l_fila][columna]
print(matrix_comparison(matriz,lienzo, "matrix to matrix"))