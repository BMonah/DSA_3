import random


class Solution(object):

    def __init__(self, w):
        self.w = w
        self.cumulative = []
        self.total = 0
        for number in w:
            self.total += number
            self.cumulative.append(self.total)

    def pickIndex(self):
        l, r = 0, len(self.cumulative)-1
        # make sure you generate a solution between idnexces 1 and self.total
        rand = random.randint(1, self.total)
        while l < r:
            mid = (l+r)//2
            if rand > self.cumulative[mid]:
                l = mid+1
            else:
                r = mid
        return l


nums = [1, 2, 3]


class Solution(object):
    def __init__(self, w):
        # Initialize the weight array and create the cumulative sum array
        self.w = w
        self.cumulative = []
        self.total = 0

        # Build the cumulative sum array
        for number in w:
            self.total += number
            self.cumulative.append(self.total)

    def pickIndex(self):
        # Generate a random number between 1 and total inclusive
        rand = random.randint(1, self.total)

        # Perform binary search to find the corresponding index
        l, r = 0, len(self.cumulative) - 1
        while l < r:
            mid = (l + r) // 2
            if rand <= self.cumulative[mid]:
                r = mid  # Narrow down the right boundary
            else:
                l = mid + 1  # Narrow down the left boundary

        return l


print(Solution(nums).randomPickWeight())
