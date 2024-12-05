class Solution:
    def wordSearch(self, board, word):
        rows, columns = len(board), len(board[0])

        def dfs(r, c, index):
            if index == len(word):
                return True

            if r < 0 or c < 0 or r >= rows or c >= columns or board[r][c] != word[index]:
                return False

            temp = board[r][c]
            board[r][c] = '#'

            results = (dfs(r+1, c, index+1) or
                       dfs(r, c+1, index+1) or
                       dfs(r-1, c, index+1) or
                       dfs(r, c-1, index+1)
                       )

            board[r][c] = temp
            return results

        for r in range(rows):
            for c in range(columns):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"

print(Solution().wordSearch(board, word))
