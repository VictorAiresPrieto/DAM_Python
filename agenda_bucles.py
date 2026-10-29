flg_00 = True #choose option
flg_01 = False #see contacts
flg_02 = False #new contact
flg_03 = False #edit contact
flg_04 = False #delete contact
flg_05 = False #search contact
salir = False #end program

#end program
while not salir:

    # choose option
    while flg_00:
        opt = input()
        if opt.isdigit():
            opt = int(opt)
            if 0 < opt < 7:
                print("valid option")
                flg_00 = False
                if opt == 1:
                    flg_01 = True
                elif opt == 2:
                    flg_02 = True
                elif opt == 3:
                    flg_03 = True
                elif opt == 4:
                    flg_04 = True
                elif opt == 5:
                    flg_05 = True
                elif opt == 6:
                    salir = True
            else:
                print("option out of range")
        else:
            print("option must be a digit")

    # see contacts
    while flg_01:
        print("seeing contacts")
        flg_01 = False

    # new contact
    while flg_02:
        print("adding contact")
        flg_02 = False

    # edit contact
    while flg_03:
        print("editing contact")

    # delete contact
    while flg_04:
        print("deleting contact")
        flg_04 = False

    # search contact
    while flg_05:
        print("searching for contact")
        flg_05 = False