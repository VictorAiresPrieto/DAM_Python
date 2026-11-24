import recurrent_functions.checkmate as check
import recurrent_functions.sorter as sort

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

separator = "*" * 50
separator_alter = "-" * 50

main_menu = ("Welcome to the User Management Program".center(50, "*") + "\n" +
             "1)Create user\n2)Modify user\n3)Show users\n4)Find user\n5)List users\n6)Exit")

repeat_receipt_menu = ("{}\n1)Continue adding receipts\n2)Exit\n{}"
                       .format(separator, separator_alter))

listing_options_menu = ("{}\n1)List by DNI\n2)List by name\n3)List by address\n4)List by purchase total\n5)Exit\n{}"
                        .format(separator, separator_alter))xº
while not b_exit:

    while flg_00:
        option = check.check_options(6, main_menu)
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

        name = ""
        number = ""
        receipt = ""

        while not check.check_type(name, "isalpha"):
            name = input("Type the contacts name: ")
        address = input("Type the contacts address: ")

        while not check.check_type(number, "isdigit"):
            number = input("Type the contacts number: ")

        while not check.check_type(receipt, "isdigit"):
            receipt = input("Type the contacts receipt: ")
            if check.check_options(2, repeat_receipt_menu) != 2:
                receipt = ""

        print(name, address, number, receipt)
        flg_01 = False
        flg_00 = True

    while flg_02:

        print("modifying user...")

        flg_02 = False
        flg_00 = True

    while flg_03:

        print("showing users...")
        flg_03 = False
        flg_00 = True

    while flg_04:
        print("finding users...")
        flg_04 = False
        flg_00 = True

    while flg_05:
        option = check.check_options(5, listing_options_menu)
        printing_list = ""
        if option == 1:
            printing_list =  sort.sorting_dict_keys(usuarios, "nombre")
            first_row = "ID"
            second_row = "Name"
        elif option == 2:
            printing_list = sort.sorting_dict_items(usuarios, "nombre", "direccion")
            first_row = "ID"
            first_row = "Name"
            second_row = "Address"
        elif option == 3:
            print("listing by address...")
        elif option == 4:
            print("listing by purchase total...")
        elif option == 5:
            flg_05 = False
            flg_00 = True
        input("{}\n{:20}{:30}\n{}\n{}{}\n"
              .format(separator, first_row, second_row, separator_alter, printing_list, separator))