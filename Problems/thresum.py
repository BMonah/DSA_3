"""
Three Integer Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:

Input: nums = [0,1,1]

Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]

Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""


class Solution:
    def threeSum(self, nums):
        res = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = [nums[i], nums[j], nums[k]]
                        res.add(tuple(tmp))
        return [list(i) for i in res]


nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))


"""
Discussion
Using two pointers
1. We need to sort the list so that we do not run on unnecessarry duplicated numbers and its easier to remove duplicates
    this will use nlogn using quicksort
2. hash the list into index and values so that we may use two pointers to arrive to the solution. the idea is that
    we have a starting value (i) and we use the left and right pointers to find the remaining two numbers
    if the sum of (i) plus the values in the two pointers is greater than 0, we move the right pointer closer
    else, we move the left pointer closer
3. if current index is not the first index and is the same as the value of previous index value, skip it
    this is because we only want unique numbers. this is skiping the value of the first element if we have a duplicate
4. do a while loop upto where left < right with below 

"""


class Solution2:
    def threeSum(self, nums):
        res = []
        nums.sort()

        for index, value in enumerate(nums):
            # Skip duplicate value for the first element
            if index > 0 and value == nums[index-1]:
                continue

            l, r = index+1, len(nums) - 1
            while l < r:
                threeSum = value + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1  # Decrease the sum by moving right pointer left
                elif threeSum < 0:
                    l += 1  # Increase the sum by moving left pointer right
                else:
                    # Found a triplet
                    res.append([value, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicate values for the left element
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    # Skip duplicate values for the right element
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return res


nums1 = [-1, 0, 1, 2, -1, -4]
nums = [0, 0, 0, 0]
print(Solution2().threeSum(nums1))


def threeSum2(nums):
    nums.sort()
    res = []
    for index, value in enumerate(nums):
        if index > 0 and nums[index] == nums[index-1]:
            continue
        l, r = index+1, len(nums)-1
        while l < r:
            if (value+nums[l]+nums[r]) > 0:
                r -= 1
            elif (value+nums[l]+nums[r]) < 0:
                l += 1
            else:
                res.append([value, nums[l], nums[r]])
                l += 1
                r -= 1

                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while l < r and nums[r] == nums[r+1]:
                    r -= 1
    return res


nums1 = [-1, 0, 1, 2, -1, -4]
print(threeSum2(nums1))


def threeSum3(nums):
    res = []
    nums.sort()
    for index, value in enumerate(nums):
        if index > 0 and nums[index] == nums[index-1]:
            continue
        l, r = index+1, len(nums)-1
        while l < r:
            thresum = value+nums[l]+nums[r]
            if thresum > 0:
                r -= 1
            elif thresum < 0:
                l += 1
            else:
                res.append([value, nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while l < r and nums[r] == nums[r+1]:
                    r -= 1
    return res


nums1 = [-1, 0, 1, 2, -1, -4]
print(threeSum3(nums1))
