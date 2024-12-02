def solution(A, B):
    # Helper function to check feasibility
    def can_form_square(side_length):
        return (A // side_length) + (B // side_length) >= 4

    # Define the search space
    low, high = 1, (A + B) // 4
    result = 0

    # Binary search
    while low <= high:
        mid = (low + high) // 2
        if can_form_square(mid):
            result = mid  # Update the result
            low = mid + 1  # Search for larger side lengths
        else:
            high = mid - 1  # Search for smaller side lengths

    return result


def solution(A, B):
    n = len(A)
    half = n // 2

    # Step 1: Unique types in each shop
    unique_A = set(A)
    unique_B = set(B)

    # Step 2: Common types between the shops
    common = unique_A & unique_B

    # Step 3: Maximum distinct types from each shop
    # Unique in A not in B
    distinct_from_A = min(len(unique_A - common), half)
    # Unique in B not in A
    distinct_from_B = min(len(unique_B - common), half)

    # Step 4: Add common types but limit the total to n
    total_distinct = distinct_from_A + distinct_from_B + len(common)
    return min(total_distinct, n)
