nums = [2, 20, 4, 10, 3, 4, 5]


def longestConsecutive(nums):
    new_nums = set(nums)
    longest = 0
    for i in nums:
        if (i-1) not in new_nums:
            length = 1
            while (i+length) in new_nums:
                length += 1
            longest = max(length, longest)
    return longest


def longestConsecutive2(nums):
    nums.sort()
    longest = 0
    current_length = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            current_length += 1
        # Skip duplicate numbers without breaking the sequence
        elif nums[i] != nums[i - 1]:
            longest = max(longest, current_length)
            current_length = 1
    return longest


print(longestConsecutive(nums))
print(longestConsecutive2(nums))
