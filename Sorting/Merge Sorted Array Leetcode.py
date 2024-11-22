class Solution(object):
    def merge(self, nums1, m, nums2, n):
        arr = []
        for i in range(0, m):
            arr.append(nums1[i])
        for i in range(0, n):
            arr.append(nums2[i])
        arr.sort()
        return arr


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

print(Solution().merge(nums1, m, nums2, n))


def microsoft(arr, num):
    num = num
    for i in arr:
        for j in arr:
            if i+j == num:
                return (i, j)


arr = [1, 2, 3, 4]
num = 3
print(microsoft(arr, num))
