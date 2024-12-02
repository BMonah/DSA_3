import heapq


class Solution:
    def kthClosest(self, points, k):
        my_heap = []
        for i, j in points:
            dist = (i*i)+(j*j)
            my_heap.append([dist, i, j])
        heapq.heapify(my_heap)
        print(my_heap)
        res = []

        while k:
            dist, i, j = heapq.heappop(my_heap)
            res.append([i, j])
            k -= 1
        return res


print(Solution().kthClosest([[0, 2], [2, 0], [2, 2]], 2))
