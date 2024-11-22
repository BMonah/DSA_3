def substring(List):
    arr = []
    max_count = 0
    count = 0
    for i in List:
        if i not in arr:
            arr.append(i)
            count += 1
            print(count)
            print(arr)
        else:
            count = 1
            arr = []
            arr.append(i)
        max_count = max(max_count, count)
    return max_count


# print(substring("abcabcbb"))


# loop through the length of the string while appending the values to an array
# append items to an array and check the length of the array
# always keep count of the length of the array and assign it a new variable
# return the maximum of all recorded length of array
# if we come across a string that is in an array
# while we still have the string in the array
# pop all the items comming before it until the actual item is removed
# append the item to the array after poping
# return the maximum recorded length of the arrays


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        arr = []
        max_count = 0
        for index in range(len(s)):
            if s[index] not in arr:
                arr.append(s[index])
                count = len(arr)
            else:
                while s[index] in arr:
                    arr.pop(0)
                arr.append(s[index])
                count = len(arr)
            max_count = max(max_count, count)
        return max_count


lcs = Solution().lengthOfLongestSubstring("abcabcbb")
print(lcs)


def lengthOfLongestAlternating(arr):
    count = 0
    max_count = 0
    for i in range(len(arr)):
        if arr[i] in (0, 1):
            if arr[i] != arr[i-1]:
                count += 1
            else:
                count = 1
        else:
            count = 0
        max_count = max(max_count, count)
    return max_count


print(lengthOfLongestAlternating(
    [1, 0, 1, 0, 1, 0, 5, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1]))

print(lengthOfLongestAlternating([0, 5, 0, 7, 0, 0, 0, 0, 1, 3, 2, 1, 0]))
