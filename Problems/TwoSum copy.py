class Solution:
    def twoSum(nums, target):
        # nums = []
        # target = int
        for i in range(0, len(nums)):
            for x in range(i+1, len(nums)):
                if nums[i] + nums[x] == target:
                    return ([i, x])
        return ('Nothing')


# test = twoSum([1, 2, 4, 9], 6)
print(Solution.twoSum([2, 7, 11, 15], 9))
# print(twoSum())
