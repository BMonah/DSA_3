def first_none_repeating(string):
    arr = []
    arr2 = []
    for i in string:
        arr.append(i)
    for j in range(0, len(arr)-1, 1):
        if arr[j] != arr[j+1]:
            arr2.append(arr[j])
    return arr2[0]


def first_non_repeating_char(string):
    my_dict = {}
    arr = []
    for i in string:
        if i not in my_dict:
            my_dict[i] = [i]
        else:
            my_dict[i].append(i)
    for i in my_dict:
        if len(my_dict[i]) == 1:
            arr.append(i)
    if arr:
        return arr[0]


string = 'leetcode'
print(first_none_repeating(string))
# print(first_non_repeating_char(string))
# print(Solution().lengthOfLongestSubstring(string))
