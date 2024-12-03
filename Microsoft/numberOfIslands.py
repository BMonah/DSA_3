class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0

        islands = 0
        row, col = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == "0":
                return

            grid[r][c] = "0"

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dfs(r+dr, c+dc)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        return islands


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(Solution().numIslands(grid2))
