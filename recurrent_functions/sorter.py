def sorting_dict_items(dict, item1_name, item2_name):
    printing_list = ""
    item1_list = dict.get(item1_name)

    return printing_list

def sorting_dict_keys(dict, item1_name):
    printing_list = ""
    dni_list = list(dict.keys())
    for j in range(len(dni_list)):
        for i in range(len(dni_list) - 1):
            if dni_list[i] > dni_list[i + 1]:
                temp = dni_list[i]
                dni_list[i] = dni_list[i + 1]
                dni_list[i + 1] = temp
    for k in range(len(dni_list)):
        printing_list = (printing_list +
                         dni_list[k].ljust(20) +
                         str(dict[dni_list[k]][item1_name]).ljust(30) + "\n")
    return printing_list