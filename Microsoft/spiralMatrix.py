class Solution:
    def spiral(matrix):
        left, right = 0, len(matrix[0])-1
        top, bottom = 0, len(matrix)-1
        result = []
        if not matrix or not matrix[0]:
            return result
        while left <= right and top <= bottom:
            for col in range(left, right+1):
                result.append(matrix[top][col])
            top += 1

            for row in range(top, bottom+1):
                result.append(matrix[row][right])
            right -= 1
            if top <= bottom:
                for col in range(right, left-1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
            if left <= right:
                for row in range(bottom, top-1, -1):
                    result.append(matrix[row][left])
                left += 1
        return result


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution.spiral(matrix))
