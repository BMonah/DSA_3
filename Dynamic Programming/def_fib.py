import heapq


class Solution:
    def happyString(a, b, c):
        res = ""
        myHeap = []
        for num, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            heapq.heappush(myHeap, (num, char))

        while myHeap:
            num, char = heapq.heappop(myHeap)

            if len(res) > 1 and res[-1] == res[-2]:
                if not myHeap:
                    break
                next_num, next_char = heapq.heappop(myHeap)
                res += next_char
                next_num += 1
                if next_num:
                    heapq.heappush(myHeap(next_num, next_char))
                heapq.heappush(myHeap, (num, char))
            else:
                res += char
                num += 1
                if num:
                    heapq.heappush(myHeap, (num, char))
        return res


print(Solution.happyString(1, 1, 7))
