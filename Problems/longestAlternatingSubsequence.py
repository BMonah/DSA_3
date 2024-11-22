def longest_alternating_subsequence(lst):
    max_length = 0
    current_length = 0
    prev = None

    for i in range(len(lst)):
        if lst[i] in [0, 1]:  # Only consider 0s and 1s
            # Check if it's the start or alternates with the previous value
            if prev is None or lst[i] != prev:
                current_length += 1
                prev = lst[i]  # Update the previous value to the current one
            else:
                current_length = 1  # Reset length if it doesn't alternate
                prev = lst[i]  # Update the previous value to the current one

            # Update the max length
            max_length = max(max_length, current_length)
        else:
            current_length = 0  # Reset if a number other than 0 or 1 is encountered
            prev = None  # Reset prev if we hit a non 0/1 value

    return max_length


# Example usage:
input_list = [0, 5, 0, 7, 0, 0, 0, 0, 1, 3, 2, 1, 0]
output = longest_alternating_subsequence(input_list)
print(output)  # Output will be 5


# loop through the array in range of its length
# check if the value of each item is either 0 or 1
# if current value is not same as previous add 1 to the counter
# if current value is the same as the previous reset current count as 1
# compare the two counts and share the maximum count
# If value is not 0 or 1
# reset current count to 0
# reset reset previous to None

def longestSubsequence(List):
    prev = None
    current_count = 0
    max_count = 0
    for i in range(len(List)):
        if List[i] in [0, 1]:
            if List[i] != prev:
                prev = List[i]
                current_count += 1
            else:
                current_count = 1
            max_count = max(max_count, current_count)
        else:
            prev = None
            current_count = 0
    return max_count


print(longestSubsequence([1, 0, 1, 0, 1, 0, 5, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1]))
print(longestSubsequence([0, 2, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1]))


# for i in range length of list
# check if i is either 0 or 1
# if i is not previous add count
# set previous to i
# else if i is not previous
# set count = 1
# set previous = i
# return maximum count recorded so far

def longestSubsequence0s1s(List):
    if not List:
        return None
    prev = List[0]
    count = 0
    max_count = 0
    for i in List:
        if i in [0, 1]:
            if i != prev:
                count += 1
            else:
                count = 1
            prev = i
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count


s1 = [0, 2, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1]
s2 = []
print(longestSubsequence0s1s(s2))


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
