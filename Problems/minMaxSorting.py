def getMinMax(arr):
    arr.sort()
    res = [arr[0], arr[-1]]
    return res

# print(getMinMax([1, 4, 7, 9, 22, 0]))


# arr = [1, 4, 7, 9, 22, 0]


def getMinMax1(arr):
    min = arr[0]
    max = arr[0]
    for i in range(0, len(arr), 1):
        if arr[i] < min:
            min = arr[i]
        elif arr[i] > max:
            max = arr[i]
    return (min, max)


def getMinMax2(arr):
    min = 0
    max = 0
    for i in arr:
        if i < min:
            min = i
        if i > max:
            max = i
    return min, max

def find_max_min(arr):
    min = max = arr[0]
    for i in arr:
        if i < min:
            min = i
        if i > max:
            max = i
    return max, min


print(getMinMax2([1, 4, 7, 9, 22, 0]))

print(getMinMax1([1, 4, 7, 9, 22, 0]))
