class Test:
    def __init__(self, nums1, m, nums2, n):
        self.nums1 = nums1
        self.n = n
        self.nums2 = nums2
        self.m = m

    def solution(self):
        arr = []
        for i in range(0, self.n):
            arr.append(self.nums1[i])
        for i in range(0, self.m):
            arr.append(self.nums2[i])
        arr.sort()
        return arr


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
mySolution = Test(nums1, n, nums2, m)
print(mySolution.solution())
