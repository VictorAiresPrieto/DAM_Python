import random

tamanno = 50

print("|" + "Ejercici1".center(tamanno, "*") + "|")

list = []
for i in range(5):
    list.append(random.randint(1, 100))

for j in range(len(list)):
    for k in range(len(list) - j - 1):
        if list[k] > list[k + 1]:
            temp = list[k]
            list[k] = list[k + 1]
            list[k + 1] = temp
print(list)

print("|" + "Ejercici2".center(tamanno, "*") + "|")

for l in range(len(list)):
    for m in range(len(list) - 1 , 0 + l , -1):
        if list[m] > list[m - 1]:
            temp = list[m - 1]
            list[m - 1] = list[m]
            list[m] = temp
print(list)

print("|" + "Ejercici3".center(tamanno, "*") + "|")

dimension = 3
matrix = []
for fila in range (dimension):
    matrix.append([])
    for columna in range (dimension):
        matrix[fila].append(random.randint(1, 100))
shown_matrix = ""
for shown_fila in range (dimension):
    for shown_columna in range (dimension):
        shown_matrix = shown_matrix + str(matrix[shown_fila][shown_columna]).rjust(4)
    shown_matrix = shown_matrix + "\n"
print(shown_matrix)

print("|" + "Ejercici4".center(tamanno, "*") + "|")

matrix_e4 = matrix.copy()
for columna in range (dimension):
    for fila in range (dimension):
        for acolumna in range (dimension - 1):
            if matrix_e4[acolumna][fila] > matrix_e4[acolumna + 1][fila]:
                temp = matrix_e4[acolumna][fila]
                matrix_e4[acolumna][fila] = matrix_e4[acolumna+1][fila]
                matrix_e4[acolumna + 1][fila] = temp

shown_matrix = ""
for shown_fila in range(dimension):
    for shown_columna in range(dimension):
        shown_matrix = shown_matrix + str(matrix_e4[shown_fila][shown_columna]).rjust(4)
    shown_matrix = shown_matrix + "\n"
print(shown_matrix)

print("|" + "Ejercici5".center(tamanno, "*") + "|")

matrix_e5 = matrix.copy()
for columna in range (dimension):
    for fila in range (dimension):
        for acolumna in range (dimension - 1, 0, -1):
            if matrix_e5[acolumna][fila] > matrix_e5[acolumna - 1][fila]:
                temp = matrix_e5[acolumna][fila]
                matrix_e5[acolumna][fila] = matrix_e5[acolumna - 1][fila]
                matrix_e5[acolumna - 1][fila] = temp

shown_matrix = ""
for shown_fila in range(dimension):
    for shown_columna in range(dimension):
        shown_matrix = shown_matrix + str(matrix_e5[shown_fila][shown_columna]).rjust(4)
    shown_matrix = shown_matrix + "\n"
print(shown_matrix)

print("|" + "Ejercici6".center(tamanno, "*") + "|")

dimension = 4
matrix = []
for fila in range (dimension):
    matrix.append([])
    for columna in range (dimension):
        matrix[fila].append(random.randint(1, 4))
shown_matrix = ""
for shown_fila in range (dimension):
    for shown_columna in range (dimension):
        shown_matrix = shown_matrix + str(matrix[shown_fila][shown_columna]).rjust(4)
    shown_matrix = shown_matrix + "\n"
print(shown_matrix)

matrix_e6 = []
for fila in range (dimension):
    matrix_e6.append([])
    for columna in range (dimension):
        matrix_e6[fila].append(0)

for fila in range (dimension):
    for columna in range (dimension):
        if matrix[fila][columna] % 2 == 0:
            for p in range(dimension):
                if p != columna:
                    matrix_e6[fila][p] = matrix_e6[fila][p] + 1

shown_matrix = ""
for shown_fila in range (dimension):
    for shown_columna in range (dimension):
        shown_matrix = shown_matrix + str(matrix_e6[shown_fila][shown_columna]).rjust(4)
    shown_matrix = shown_matrix + "\n"
print(shown_matrix)