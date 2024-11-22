class BinarySearch:
    def binarySearch(self, nums, target):
        l, r = 0, len(nums)+1

        while l < r:
            middle = (l+r)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                l = middle + 1
            else:
                r = middle - 1
        return -1


nums = [-1, 0, 2, 4, 6, 8]
print(BinarySearch().binarySearch(nums, 4))
