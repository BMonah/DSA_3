from collections import deque


class Solution:
    def productExceptSelf(self, num):
        n = 1
        m = 1
        prefix = []
        postfix = [None for i in range(len(num))]
        for i in range(len(num)):
            n *= num[i]
            prefix.append(n)
        for j in range(len(num)-1, -1, -1):
            m *= num[j]
            postfix[j] = m
        print(prefix, postfix)
        for i in range(len(num)):
            if i == 0:
                num[i] = postfix[i+1]
            elif i == len(num)-1:
                num[i] = prefix[i-1]
            else:
                num[i] = prefix[i-1] * postfix[i+1]
        return num


nums = [1, 2, 3, 4]
print(len(nums))
print(Solution().productExceptSelf(nums))
