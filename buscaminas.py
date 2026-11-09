import random

dimension = 10
sbi = 3
lifes = 3
#Space Between Index

exit = False
game_ended = False
flg_00 = True
flg_01 = False
flg_010 = False
flg_011 = False

margin = dimension * sbi - (sbi - 1)
opt_menu = ("MINESWEEPER".center(margin, "*").rjust(dimension * sbi) + "\n"
            + " " * (sbi - 1) + "1)New Game" + "\n"
            + " " * (sbi - 1) + "2)Exit" + "\n"
            + " " * (sbi - 1) + ("*"*margin) + "\n"
            + " " * (sbi - 1))
game_menu = ("MINESWEEPER".center(margin, "*").rjust(dimension * sbi) + "\n"
            + "{}")

while not exit:
    while flg_00:
        opt = input("{}Choose an option: ".format(opt_menu))
        if opt.isdigit():
            opt = int(opt)
            if 0 < opt < 3:
                flg_00 = False
                if opt == 1:
                    flg_01 = True
                else:
                    exit = True
            else:
                print("*" * (sbi - 1) + "Index out of range")
        else:
            print(" " * (sbi - 1) + "Not numeric option")

    while flg_01:
        # crear matriu jugador
        shown_matrix = []
        for row in range(dimension):
            shown_matrix.append([])
            for column in range(dimension):
                shown_matrix[row].append("X")

        # crear matriu interna
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
                            if 0 <= row + height < dimension and 0 <= column + width < dimension:
                                if actual_matrix[row + height][column + width] != "M":
                                    actual_matrix[row + height][column + width] \
                                        = actual_matrix[row + height][column + width] + 1
        while not game_ended:
            flg_010 = True
            flg_011 = True
            lifes_shown = (("--(0)--"*lifes).center(margin, "-"))
            print(game_menu.format((" " * (sbi - 1)) + lifes_shown))
            while flg_010:
                flg_010 = False

            game_ended = True

        #mostrar matriu
        datos = ""
        final_fila = -1
        for row in range(len(actual_matrix)):
            for column in range(len(actual_matrix[row])):
                datos = datos + str(actual_matrix[row][column]).rjust(sbi)
            datos = datos + "|".rjust(sbi)
            for column in range(len(shown_matrix[row])):
                datos = datos + str(shown_matrix[row][column]).rjust(sbi)
            datos = datos + "\n"

        print(datos)
        flg_01 = False
        flg_00 = True



