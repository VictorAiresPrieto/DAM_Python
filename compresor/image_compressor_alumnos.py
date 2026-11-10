import random

from PIL import Image

import AWS_compression as amsc

# ruta_imagen = input("Ruta o nombre de la imagen a comprimir:\n")
# ruta_imagen_comprimida = input("Ruta o nombre de la imagen comprimida:\n")
ruta_imagen = "logo_esteve.jpeg"
ruta_imagen_comprimida = "aa_logo_comprimido.jpg"
comprimida_r = []
comprimida_g = []
comprimida_b = []
comprimida_r_alter = []
comprimida_g_alter = []
comprimida_b_alter = []
comprimida_r_alter2 = []
comprimida_g_alter2 = []
comprimida_b_alter2 = []
# Leer imagen
matriz_r, matriz_g, matriz_b, ancho, alto = amsc.imagen_a_matrices(ruta_imagen)


######################################################################
##### ESCRIBE TU CÓDIGO DE COMPRESIÓN DE IMÁGENES A CONTINUACIÓN #####
######################################################################
for fila in range(0,ancho,2):
    comprimida_r.append([])
    comprimida_g.append([])
    comprimida_b.append([])
    for columna in range(0,alto,2):
        if len(matriz_b)%2 == 1 and (columna == len(matriz_b) - 1 or fila == len(matriz_r) - 1):
            comprimida_r[fila//2].append(matriz_r[fila][columna])
            comprimida_g[fila//2].append(matriz_g[fila][columna])
            comprimida_b[fila//2].append(matriz_b[fila][columna])
        else:
            comprimida_r[fila//2].append((matriz_r[fila][columna] + matriz_r[fila+1][columna+1] + matriz_r[fila+1][columna] + matriz_r[fila][columna+1])//4)
            comprimida_g[fila//2].append((matriz_g[fila][columna] + matriz_g[fila+1][columna+1] + matriz_g[fila+1][columna] + matriz_g[fila][columna+1])//4)
            comprimida_b[fila//2].append((matriz_b[fila][columna] + matriz_b[fila+1][columna+1] + matriz_b[fila+1][columna] + matriz_b[fila][columna+1])//4)
for fila in range(ancho):
    comprimida_r_alter.append([])
    comprimida_g_alter.append([])
    comprimida_b_alter.append([])
    for columna in range(0,alto,2):
        if len(matriz_b)%2 == 1 and columna == len(matriz_b) - 1:
            comprimida_r_alter[fila].append(matriz_r[fila][columna])
            comprimida_g_alter[fila].append(matriz_g[fila][columna])
            comprimida_b_alter[fila].append(matriz_b[fila][columna])
        else:
            comprimida_r_alter[fila].append((matriz_r[fila][columna] + matriz_r[fila][columna+1])//2)
            comprimida_g_alter[fila].append((matriz_g[fila][columna] + matriz_g[fila][columna+1])//2)
            comprimida_b_alter[fila].append((matriz_b[fila][columna] + matriz_b[fila][columna+1])//2)
for fila in range(0,ancho,2):
    comprimida_r_alter2.append([])
    comprimida_g_alter2.append([])
    comprimida_b_alter2.append([])
    for columna in range(alto//2):
        if len(matriz_b)%2 == 1 and fila == len(matriz_r) - 1:
            comprimida_r_alter2[fila//2].append(comprimida_r_alter[fila][columna])
            comprimida_g_alter2[fila//2].append(comprimida_g_alter[fila][columna])
            comprimida_b_alter2[fila//2].append(comprimida_b_alter[fila][columna])
        else:
            comprimida_r_alter2[fila//2].append((comprimida_r_alter[fila][columna] + comprimida_r_alter[fila+1][columna])//2)
            comprimida_g_alter2[fila//2].append((comprimida_g_alter[fila][columna] + comprimida_g_alter[fila+1][columna])//2)
            comprimida_b_alter2[fila//2].append((comprimida_b_alter[fila][columna] + comprimida_b_alter[fila+1][columna])//2)


# Las matrices de la imagen original son matriz_r, matriz_g y matriz_b
# una para cada canal.
# Crea tres matrices nuevas llamadas: comprimida_r, comprimida_g y
# comprimida_b con el fin de comprimir las matrices de la imagen 
# original.
# Utiliza los diferentes métodos de compresión explicados por el 
# profesor en clase.

######################################################################
##### FINAL DE TU CÓDIGO DE COMPRESIÓN DE IMÁGENES ###################
######################################################################

# Mostrar estadísticas de compresión
amsc.mostrar_stats(matriz_r, matriz_g, matriz_b, comprimida_r, comprimida_g, comprimida_b)
amsc.mostrar_stats(matriz_r, matriz_g, matriz_b, comprimida_r_alter, comprimida_g_alter, comprimida_b_alter)
amsc.mostrar_stats(matriz_r, matriz_g, matriz_b, comprimida_r_alter2, comprimida_g_alter2, comprimida_b_alter2)
# Guardar matriz comprimida
amsc.matrices_a_imagen(comprimida_r, comprimida_g, comprimida_b, "images/" + ruta_imagen_comprimida)
amsc.matrices_a_imagen(comprimida_r_alter, comprimida_g_alter, comprimida_b_alter, "images/alter_" + ruta_imagen_comprimida)
amsc.matrices_a_imagen(comprimida_r_alter2, comprimida_g_alter2, comprimida_b_alter2, "images/alter_2_" + ruta_imagen_comprimida)

