import heapq


class Solution:
    def lastStoneWeight(self, stones):

        my_heap = [-stones for stones in stones]
        heapq.heapify(my_heap)
        print(my_heap)
        while len(my_heap) > 1:
            next = 0
            largest = -heapq.heappop(my_heap)
            next_largest = -heapq.heappop(my_heap)
            print(largest, next_largest)
            if largest == next_largest:
                next = 0
            elif largest > next_largest:
                next = largest - next_largest
            elif next_largest < largest:
                next = next_largest - largest
            heapq.heappush(my_heap, -next)
            print(my_heap)
        return -my_heap[0]


print(Solution().lastStoneWeight([2, 3, 6, 2, 4]))
