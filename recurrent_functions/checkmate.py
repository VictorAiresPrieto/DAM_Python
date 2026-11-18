def check_options(options):
    option = input("Option: ")
    if check_type(option,"isdigit"):
        option = int(option)
        for i in range(1,options+1):
            if option == i:
                break
            elif i == options:
                print("Index out of range")
                option = -1
    else:
        print("Not a valid input")
        option = -1
    return option

def check_type(b_value, b_type):
    is_valid = False
    if b_type == "isdigit":
        if b_value.isdigit():
            is_valid = True
    elif b_type == "isalpha":
        if b_value.isalpha():
            is_valid = True
    return is_valid