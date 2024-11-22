def item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        if i not in my_dict:
            my_dict[i] = None
    for j in list2:
        if j in my_dict:
            return True
    return False
