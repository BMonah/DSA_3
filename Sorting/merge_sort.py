def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the array in half
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    sorted_array = []
    i = j = 0

    # Compare elements from left and right halves and merge them
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # If there are remaining elements in left, add them
    while i < len(left):
        sorted_array.append(left[i])
        i += 1

    # If there are remaining elements in right, add them
    while j < len(right):
        sorted_array.append(right[j])
        j += 1

    return sorted_array


# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)  # Output: [3, 9, 10, 27, 38, 43, 82]
