import random

dimension = 10

#crear matriu jugador
shown_matrix = []
for row in range(dimension):
    shown_matrix.append([])
    for column in range(dimension):
        shown_matrix[row].append("X")

#crear matriu interna
actual_matrix = []
for row in range(dimension):
    actual_matrix.append([])
    for column in range(dimension):
        actual_matrix[row].append(0)
        prob = 10
        borders_left = 8
        top_checked = False
        if random.randint(1, 100) <= prob:
            actual_matrix[row][column] = "M"

for row in range(dimension):
    for column in range(dimension):
        if actual_matrix[row][column] == "M":
            for height in range(-1, 2):
                for width in range(-1, 2):
                    if 0 <= row+height < dimension and 0 <= column+width < dimension:
                        if actual_matrix[row + height][column + width] != "M":
                            actual_matrix[row + height][column + width] = actual_matrix[row + height][column + width] + 1

#mostrar matriu
datos = ""
final_fila = -1
for row in range(len(actual_matrix)):
    for column in range(len(actual_matrix[row])):
        datos = datos + str(actual_matrix[row][column]).rjust(5)
    datos = datos + "|".rjust(5)
    for column in range(len(shown_matrix[row])):
        datos = datos + str(shown_matrix[row][column]).rjust(5)
    datos = datos + "\n"
print(datos)



