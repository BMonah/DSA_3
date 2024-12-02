class Solution:
    def nextGreaterElement(self, n):
        # we want a list of string elements in the number
        digits = list(str(n))
        length = len(digits)

        pivot = -1

        # find the pivot
        for i in range(length-2, -1, -1):
            if digits[i] < digits[i+1]:
                pivot = i
                break

        if pivot == -1:
            return -1

        # loop through the whole string array from the right
        # switch value of pivot and the greater one to get the least possible
        # highest value with the same digits
        for j in range(length-1, pivot, -1):
            if digits[j] > digits[pivot]:
                digits[j], digits[pivot] = digits[pivot], digits[j]
                break

        # reverse the suffix to ge the least value from the pivot location, reverse to ascending order
        digits = digits[:pivot+1] + digits[pivot+1:][::-1]

        result = int("".join(digits))

        return result if result <= (2**31-1) else -1


n1 = 4213
n2 = 12
n3 = 1
n4 = 45654312
n5 = 2147483476

print(Solution().nextGreaterElement(n5))


class Solution:
    def nextGreater(self, n):
        digits = list(str(n))

        pivot = -1

        for i in range(len(digits)-2, -1, -1):
            if digits[i] < digits[i+1]:
                pivot = i
                break

        if pivot == -1:
            return -1

        for j in range(len(digits)-1, pivot, -1):
            if digits[j] > digits[pivot]:
                digits[pivot], digits[j] = digits[j], digits[pivot]
                print(digits)
                break

        digits = digits[:pivot+1]+digits[pivot+1:][::-1]
        result = int("".join(digits))

        return result if result <= (2**31-1) else -1


print(Solution().nextGreater(n5))

print(2**31-1)
