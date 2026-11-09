import random
import time

lienzo = []
dimension = 10
sbi = 4
fila = random.randint(0, dimension-1)
columna = random.randint(0, dimension-1)
x_direction = random.randrange(-1, 2,2)
y_direction = random.randrange(-1, 2, 2)

for l_fila in range(dimension):
    lienzo.append([])
    for l_columna in range(dimension):
        lienzo[l_fila].append(0)
        if fila == l_fila and columna == l_columna:
            lienzo[l_fila][l_columna] = "X"

while True:
    lienzo[fila][columna] = 0
    if fila+x_direction == dimension or fila+x_direction == -1:
        x_direction = x_direction * (-1)
    if columna+y_direction == dimension or columna+y_direction == -1:
        y_direction = y_direction * (-1)

    fila = fila + x_direction
    columna = columna + y_direction
    lienzo[fila][columna] = "X"
    datos = ""
    final_fila = -1
    for row in range(len(lienzo)):
        for column in range(len(lienzo[row])):
            datos = datos + str(lienzo[row][column]).rjust(sbi)
        datos = datos + "\n"
    print(datos)
    time.sleep(1)
