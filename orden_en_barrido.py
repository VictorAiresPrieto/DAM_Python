import random
from matrix import matrix_comparison as mt
numbers = []
for k in range(10):
    numbers.append(random.randrange(-100, 100))
for pasada in range(len(numbers)-1):
    ordenado = True
    for i in range(len(numbers)-1-pasada):
        if numbers[i] > numbers[i+1]:
            ordenado = False
            temp = numbers[i]
            numbers[i] = numbers[i+1]
            numbers[i+1] = temp
    if ordenado:
        break
print(numbers)

#para una matriz por filas
numbers_matrix = []
numbers_matrix_original = []
for k in range(10):
    numbers_matrix.append([])
    numbers_matrix_original.append([])
    for l in range(10):
        temp_random_num = random.randrange(-100, 100)
        numbers_matrix[k].append(temp_random_num)
        numbers_matrix_original[k].append(temp_random_num)
for fila  in range(len(numbers_matrix)):
    for pasada in range(len(numbers_matrix)-1):
        ordenado = True
        for i in range(len(numbers_matrix)-1-pasada):
            if numbers_matrix[fila][i] > numbers_matrix[fila][i+1]:
                ordenado = False
                temp = numbers_matrix[fila][i]
                numbers_matrix[fila][i] = numbers_matrix[fila][i+1]
                numbers_matrix[fila][i+1] = temp
        if ordenado:
            break
print(mt(numbers_matrix_original,numbers_matrix, "matrix to matrix"))

#para una matriz por columnas
numbers_matrix = []
numbers_matrix_original = []
for k in range(10):
    numbers_matrix.append([])
    numbers_matrix_original.append([])
    for l in range(10):
        temp_random_num = random.randrange(-100, 100)
        numbers_matrix[k].append(temp_random_num)
        numbers_matrix_original[k].append(temp_random_num)
for columna in range(len(numbers_matrix)):
    for pasada in range(len(numbers_matrix)-1):
        ordenado = True
        for i in range(len(numbers_matrix)-1-pasada):
            if numbers_matrix[i][columna] > numbers_matrix[i+1][columna]:
                ordenado = False
                temp = numbers_matrix[i][columna]
                numbers_matrix[i][columna] = numbers_matrix[i+1][columna]
                numbers_matrix[i+1][columna] = temp
        if ordenado:
            break
print(mt(numbers_matrix_original,numbers_matrix, "matrix to matrix"))

#para una matriz por filas al reves
numbers_matrix = []
numbers_matrix_original = []
for k in range(10):
    numbers_matrix.append([])
    numbers_matrix_original.append([])
    for l in range(10):
        temp_random_num = random.randrange(-100, 100)
        numbers_matrix[k].append(temp_random_num)
        numbers_matrix_original[k].append(temp_random_num)
for fila  in range(len(numbers_matrix)):
    for pasada in range(len(numbers_matrix)):
        ordenado = True
        for i in range(len(numbers_matrix)-1, pasada , -1):
            if numbers_matrix[fila][i] < numbers_matrix[fila][i-1]:
                ordenado = False
                temp = numbers_matrix[fila][i]
                numbers_matrix[fila][i] = numbers_matrix[fila][i-1]
                numbers_matrix[fila][i-1] = temp
        if ordenado:
            break
print(mt(numbers_matrix_original,numbers_matrix, "matrix to matrix"))

#para una matriz por columnas al reves
numbers_matrix = []
numbers_matrix_original = []
for k in range(10):
    numbers_matrix.append([])
    numbers_matrix_original.append([])
    for l in range(10):
        temp_random_num = random.randrange(-100, 100)
        numbers_matrix[k].append(temp_random_num)
        numbers_matrix_original[k].append(temp_random_num)
for columna in range(len(numbers_matrix)):
    for pasada in range(len(numbers_matrix)):
        ordenado = True
        for i in range(len(numbers_matrix)-1, pasada, -1):
            if numbers_matrix[i][columna] > numbers_matrix[i-1][columna]:
                ordenado = False
                temp = numbers_matrix[i][columna]
                numbers_matrix[i][columna] = numbers_matrix[i-1][columna]
                numbers_matrix[i-1][columna] = temp
        if ordenado:
            break
print(mt(numbers_matrix_original,numbers_matrix, "matrix to matrix"))