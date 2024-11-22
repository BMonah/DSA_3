def find_duplicates(nums):
    num_counts = {}
    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1
    duplicates = []
    for num, count in num_counts.items():
        if count > 1:
            duplicates.append(num)
    return duplicates


def find_duplicate(arr):
    my_dict = {}
    stack = []
    for i in arr:
        if i not in my_dict:
            my_dict[i] = [i]
        else:
            my_dict[i].append(i)
    print(my_dict)
    for j in my_dict:
        if len(my_dict[j]) > 1:
            stack.append(my_dict[j])
    return stack


def duplicates(arr):
    dictionary = {}
    stack = []
    for i in arr:
        if i not in dictionary:
            dictionary[i] = [i]
        else:
            dictionary[i].append(i)
    for i in list(dictionary.values()):
        if len(i) > 1:
            stack.append(i)
    return stack


# the time complexity for sorting is o(nlogn)
# space complexity is o(1)
def find_duplicates(arr):
    sorted_list = sorted(arr)
    arr = []
    for i in range(0, len(sorted_list)-1):
        if sorted_list[i] == sorted_list[i+1]:
            arr.append(sorted_list[i])
    if arr:
        return True
    else:
        return False


def containtsDuplicate(nums):
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)


c = [5, 7, 9, 10]
b = [1, 2, 4, 5, 5, 5, 4, 9, 6, 9, 6]
# print(find_duplicate(b))
print(duplicates(b))
# print(find_duplicates(b))
print(find_duplicates(b))
print(containtsDuplicate(b))
