"""
Top K Elements in List
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
"""

# 1 arrange the numbers in a dictionary where key is number and value is the number of times it appears in the list
# create a list of arrays within an array where the length of the list is the length of nums + 1
# we do this as we want to insert numbers in the index list where the index represents the number of times it appears
# loop through the frequency list while appending contents of each index to a result array
# if the length of the result array is equal to k, return the result array


class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        res = []

        for number in nums:
            # we want to map the numbers to the number of times they appear,
            # if the number is not present add 1 to 0
            count[number] = 1 + count.get(number, 0)

        # Insert the frequency of which the count appears into the index
        # and append the number in the index of the frequency tracker
        for number, count in count.items():
            freq[count].append(number)

        # loop through the freq list to get top k elements
        for index in range(len(freq) - 1, 0, -1):
            print(freq[index], index)
            for n in freq[index]:
                print(n)
                res.append(n)
                if len(res) == k:
                    return res


nums = [1, 2, 2, 3, 3, 3, 17, 17, 17]
k = 2

print(Solution().topKFrequent(nums, k))
