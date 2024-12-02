import heapq


class Solution:
    def findKthLargest(self, nums, k):
        my_heap = [-i for i in nums]
        heapq.heapify(my_heap)

        while k:
            kth_largest = -heapq.heappop(my_heap)
            k -= 1
        return kth_largest

    def usingSorting(self, nums, k):
        nums.sort()
        return nums[len(nums)-k]


print(Solution().findKthLargest([2, 3, 1, 5, 4], 2))
