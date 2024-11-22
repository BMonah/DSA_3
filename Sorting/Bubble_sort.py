def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list


def bubble_sort2(my_list):
    for i in range(0, len(my_list)):
        for j in range(i+1, len(my_list)):
            if my_list[i] > my_list[j]:
                temp = my_list[i]
                my_list[i] = my_list[j]
                my_list[j] = temp
    return my_list


print(bubble_sort2([2, 7, 29, 1, 13, 39, 12, 8]))
