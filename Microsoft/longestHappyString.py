import heapq


class Solution:
    def longestDiverseString(self, a, b, c):
        res, maxHeap = "", []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(maxHeap, (count, char))

        while maxHeap:
            # this will make sure we always pop the lowest count, towards the -ve
            count, char = heapq.heappop(maxHeap)

            # add the character to the result
            if len(res) > 1 and res[-1] == res[-2] == char:
                # if the last two characters are the same as the current one,
                # we need to take the next most frequent character
                if not maxHeap:
                    break  # only if we have no other character to use
                # if we have another character to use
                next_count, next_char = heapq.heappop(maxHeap)
                res += next_char
                # Increament the count towards zero to track times the character should appear
                next_count += 1

                # if there are still characters left for next_char, push it back into the heap
                if next_count:
                    heapq.heappush(maxHeap, (next_count, next_char))

                heapq.heappush(maxHeap, (count, char))
            else:  # if an empty string or res[-1] != res[-2]
                res += char  # add the character to res
                count += 1
                if count:
                    heapq.heappush(maxHeap, (count, char))
        return res


print(Solution().longestDiverseString(2, 1, 7))
