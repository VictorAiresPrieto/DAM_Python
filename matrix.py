import random


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
print(datos)

print("   -----------------")
#MATRIZ INVERTIDA COLUMNAS
datos = ""
for fila in range(dimension):
    #print(columna)
    for columna in range(dimension-1, -1, -1):
        #print(fila)
        datos = datos + str(matriz[fila][columna]).rjust(5)
    datos = datos + "\n"
print(datos)

print("   -----------------")
#MATRIZ INVERTIDA FILAS
datos = ""
for fila in range(dimension-1, -1, -1):
    #print(columna)
    for columna in range(dimension):
        #print(fila)
        datos = datos + str(matriz[fila][columna]).rjust(5)
    datos = datos + "\n"
print(datos)

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
print(datos)