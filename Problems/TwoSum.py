class Solution:
    def twoSum(nums, target):
        # nums = []
        # target = int
        for i in range(0, len(nums)):
            for x in range(i+1, len(nums)):
                if nums[i] + nums[x] == target:
                    return ([i, x])
        return ('Nothing')


def twosum(nums, target):
    my_dic = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in my_dic:
            return (num, complement)
        else:
            my_dic[num] = index


def twosum4(nums, target):
    arr = []
    for i in nums:
        complement = target - i
        if complement in arr:
            return (complement, i)
        else:
            arr.append(i)

# return index of the smallest value first


class Solution:
    def twoSum(self, nums, target):
        my_dic = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in my_dic:
                return [my_dic[complement], index]
            my_dic[value] = index


test = 'newString.two'
print(test.split('.')[1])

print(Solution().twoSum([11, 11, 2, 15, 7], 9))


# print(twosum([11, 11, 2, 15, 7], 9))
# print(twosum4([11, 11, 2, 15, 7], 9))

# print(twoSum2([2, 11, 15, 9], 9))
# test = twoSum([1, 2, 4, 9], 6)
# print(Solution.twoSum([2, 7, 11, 15], 9))
# print(twoSum())


'''
0 2
{2: 0}
1 7
{2: 0, 7: 1}
2 11
{2: 0, 7: 1, 11: 2}
3 15
{2: 0, 7: 1, 11: 2, 15: 3}
'''
