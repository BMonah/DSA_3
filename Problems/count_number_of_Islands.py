"""
Count Number of Islands
Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.
An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. 
You may assume water is surrounding the grid (i.e., all the edges are water).

Example 1:

Input: grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
Output: 1
Example 2:

Input: grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
Output: 4
"""


"""
1. initialize the limit of the rows and columns in the graph/matrix
    initialize islands = 0
    initialize visited = visited so that we do not repeate ourselves
2. Perform a BFS/DFS on the graph recording the visited rows and columns
    a. for row in total rows, for column in total columns, if value == 1, increase island count and perform a BFS to capture all ones


"""


class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        total_rows, total_cols = len(grid), len(grid[0])
        print(total_rows, total_cols)
        visit = set()
        islands = 0

        def bfs(row, column):
            q = [(row, column)]  # Initialize the queue with the starting point
            visit.add((row, column))

            # Define movement directions
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            while q:
                current_row, current_column = q.pop(
                    0)  # Get the current position

                for dr, dc in directions:  # Iterate over all directions
                    new_row, new_column = current_row + dr, current_column + dc

                    # Check if the new position is valid and is land
                    if (new_row in range(total_rows) and
                        new_column in range(total_cols) and
                        (new_row, new_column) not in visit and
                            grid[new_row][new_column] == "1"):
                        # Add new position to the queue
                        q.append((new_row, new_column))
                        visit.add((new_row, new_column))  # Mark as visited

        for row in range(total_rows):
            for column in range(total_cols):
                # Found unvisited land
                if grid[row][column] == "1" and (row, column) not in visit:
                    bfs(row, column)  # Perform BFS to mark the entire island
                    islands += 1  # Increment the island count

        return islands


grid = [
    ["1", "1", "0", "0", "1"],
    ["1", "1", "0", "0", "1"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(Solution().numIslands(grid))
