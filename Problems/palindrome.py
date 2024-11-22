def isPalindrome(value):
    arr1 = []
    arr2 = []
    value = ''.join(char for char in value.lower() if char.isalnum())
    for i in range(0, len(value), 1):
        arr1.append(value[i])
    for i in range(len(value)-1, -1, -1):
        arr2.append(value[i])
    print(arr1, arr2)
    if arr1 == arr2:
        return True
    return False


print(isPalindrome('-12321-'))
print(isPalindrome("Was it a car or a cat I saw"))


# Using two pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        value = ''.join(char for char in s.lower() if char.isalnum())
        l, r = 0, len(value)-1
        while l < r:
            if value[l] != value[r]:
                return False
            l, r = l+1, r-1
        return True
