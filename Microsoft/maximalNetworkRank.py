class Solution:
    def maximalNetwork(self, n, roads):
        count = [0] * n
        road_map = {}

        for a, b in roads:
            count[a] += 1
            count[b] += 1
            road_map[(a, b)] = True
            road_map[(b, a)] = True

        maximal_rank = 0

        for i in range(n):
            for j in range(i+1, n):
                rank = count[i] + count[j]
                if (i, j) in road_map or (j, i) in road_map:
                    rank -= 1
                maximal_rank = max(maximal_rank, rank)

        return maximal_rank


roads = [[0, 1], [0, 3], [1, 2], [1, 3]]
n = 4

print(Solution().maximalNetwork(n, roads))
