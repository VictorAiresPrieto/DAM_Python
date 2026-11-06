import random

def matrix_comparison(original_matrix,edited_matrix):
    datos = ""
    final_fila = -1
    for fila in range(len(original_matrix)):
        for columna in range(len(original_matrix[fila])):
            datos = datos + str(original_matrix[fila][columna]).rjust(5)
        datos = datos + "|".rjust(4)

        inicio_fila = final_fila + 1
        final_fila = edited_matrix.find("\n",inicio_fila)
        datos = datos + edited_matrix[inicio_fila:final_fila]
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

print(matrix_comparison(matriz,datos))

print("   -----------------")
#MATRIZ INVERTIDA COLUMNAS
datos = ""
for fila in range(dimension):
    #print(columna)
    for columna in range(dimension-1, -1, -1):
        #print(fila)
        datos = datos + str(matriz[fila][columna]).rjust(5)
    datos = datos + "\n"
print(matrix_comparison(matriz,datos))

print("   -----------------")
#MATRIZ INVERTIDA FILAS
datos = ""
for fila in range(dimension-1, -1, -1):
    #print(columna)
    for columna in range(dimension):
        #print(fila)
        datos = datos + str(matriz[fila][columna]).rjust(5)
    datos = datos + "\n"
print(matrix_comparison(matriz,datos))

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
print(matrix_comparison(matriz,datos))