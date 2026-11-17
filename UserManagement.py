import recurrent_functions.checkmate as check

letrasDni = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
usuario1 = {"nombre":"Pedro Javier Morales",  "direccion": "Flores 36 8º 2º", "tfn":["+0034345345345"],"compras":[1234,423,23]}
usuario2 = {"nombre":"Maite Lopez Miravet", "direccion":"Balmes 31 1º 2º","tfn":["+0034234234235","+0034239999235"],"compras":[12344]}
usuario3 = {"nombre":"Marta Garcia Suarez",  "direccion":"Valencia 21 3º 1º","tfn": ["+0075766576575"],"compras":[34,423,23,6]}
usuarios = {"47474747X":usuario1,"24536425T":usuario2,"76767676H":usuario3}

b_exit = False
flg_00 = True
flg_01 = False
flg_02 = False
flg_03 = False
flg_04 = False
flg_05 = False

while not b_exit:
    while flg_00:
        option = check.check_options(6)
        if option == 1:
            flg_00 = False
            flg_01 = True
        elif option == 2:
            flg_00 = False
            flg_02 = True
        elif option == 3:
            flg_00 = False
            flg_03 = True
        elif option == 4:
            flg_00 = False
            flg_04 = True
        elif option == 5:
            flg_00 = False
            flg_05 = True
        elif option == 6:
            flg_00 = False
            b_exit = True

    while flg_01:
        nombre = ""
        number = ""
        receipt = ""
        more_receipts = True
        while not check.check_type(nombre, "isalpha"):
            nombre = input("Type the contacts name: ")
        address = input("Type the contacts address: ")
        while not check.check_type(number, "isdigit"):
            number = input("Type the contacts number: ")
        while more_receipts:
            while not check.check_options(2)
            while not check.check_type(receipt, "isdigit"):
                receipt = input("Type the contacts receipt: ")




