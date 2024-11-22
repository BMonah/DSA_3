# determine whether the two lists have a common item
def checkList(arr1, arr2):
    for i in arr1:
        for j in arr2:
            if i == j:
                print(i)


def checkList2(arr1, arr2):
    for i in arr2:
        if i in arr1:
            print(i)


def item_in_common(arr1, arr2):
    my_dict = {}
    for i in arr1:
        my_dict[i] = True

    for j in arr2:
        if j in my_dict:
            return True
    return False


arr1 = [1, 3, 5]
arr2 = [2, 4, 5, 3]
# checkList(arr1, arr2)
print(item_in_common(arr1, arr2))
# checkList2(arr1, arr2)
