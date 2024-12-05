from collections import defaultdict


class Solution:
    def cinemaReservation(self, n, reservedSeats):
        reserved = defaultdict(set)

        for row, seats in reservedSeats:
            reserved[row].add(seats)

        group = 0

        for row in reserved:
            reservations = reserved[row]
            left = all(seats not in reservations for seats in range(2, 6))
            middle = all(seats not in reservations for seats in range(4, 8))
            right = all(seats not in reservations for seats in range(6, 10))

            if left and right:
                group += 2
            elif left or middle or right:
                group += 1

        group += (n-len(reserved))*2
        return group


reservedSeats = [[2, 1], [1, 8], [2, 6]]
reservedSeats2 = [[4, 3], [1, 4], [4, 6], [1, 7]]

print(Solution().cinemaReservation(4, reservedSeats2))


class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = n
        col = 12

        grid = [[0 for _ in range(col)] for _ in range(rows)]

        for r in range(rows):
            for c in range(col):
                if grid[r][c] in reservedSeats:
                    grid[r][c] = 'X'

        for r in range(rows):
            for c in range(col):
                if c in (4, 8):
                    grid[r][c] = 'A'

        count = 0
        for r in range(rows):
            for c in range(col):
                if grid[r][c] not in ('X', 'A'):
                    count += 1
        return count
