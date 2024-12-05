class Solution:
    def minimumMoves(self, nums):
        minimum = min(nums)

        total = sum(nums)

        moves = total-(minimum*len(nums))

        return moves


print(Solution().minimumMoves([1, 2, 3, 4]))
