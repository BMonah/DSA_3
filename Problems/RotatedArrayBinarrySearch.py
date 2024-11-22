class Solution:
    def findMin(self,  nums):
        # initial assumption is that the first value is the smallest
        minimum = nums[0]
        l, r = 0, len(nums)-1

        while l < r:
            if nums[l] < nums[r]:  # This means the subquery is sorted, so return the minimum at l
                minimum = min(minimum, nums[l])
                break  # No need to continue searching if it's sorted

            middle = (l+r)//2  # middle index
            # update the result of the smallest value so far
            minimum = min(minimum, nums[middle])
            if nums[middle] >= nums[l]:
                # if nums[m] is greater than or equal to nums[l], the minimum is in the right part
                l = middle + 1
            else:
                # if nums[m] is less than nums[l], the minimum is in the left part
                r = middle - 1
        # Final comparison to account for the smallest element
        return min(minimum, nums[l])

    def findmin2(self, nums):
        minimum = nums[0]
        l, r = 0, len(nums)-1

        while l < r:
            if nums[l] < nums[r]:
                minimum = min(nums[l], nums[0])
                break

            middle = (l+r)//2
            minimum = min(nums[middle], nums[l])

            if nums[middle] >= nums[l]:
                l = middle + 1
            else:
                r = middle - 1
        return min(minimum, nums[l])

    def findmin3(self, nums):
        minimum = nums[0]
        for number in nums:
            if number < minimum:
                minimum = number
        return minimum


num = [3, 4, 5, 6, 1, 2]
print(Solution().findMin(num))
print(Solution().findmin2(num))
print(Solution().findmin3(num))
