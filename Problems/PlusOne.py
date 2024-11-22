class Solution(object):
    def plusOne(self, digits):
        string = []
        for i in digits:
            string.append(str(i))
        digits = ''.join(string)
        digits = str(int(digits) + 1)
        res = []
        for i in digits:
            res.append(int(i))
        return res


print(Solution().plusOne([128, 1]))


def plusone2(num):
    arr = []
    arr2 = []
    for i in num:
        arr.append(str(i))
    new_num = int(''.join(arr)) + 1
    for i in str(new_num):
        arr2.append(int(i))
    return arr2


print(plusone2([1, 2, 9]))
