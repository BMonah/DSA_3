def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp < my_list[j] and j >= 0:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list


print(insertion_sort([2, 7, 29, 1, 13, 39, 12, 8]))

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
i = 0

while i < len(my_list):
    print(my_list[i])
    i += 3
