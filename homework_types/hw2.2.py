def swap_dict(dicti):
    list_from_dict = list(dicti.items())
    list_reverse = []
    for i in list_from_dict:
        list_reverse.append(i[::-1])
    dict_swap = dict(list_reverse)
    return dict_swap