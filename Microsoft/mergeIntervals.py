class Solution:
    def merge(self, intervals):
        # sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        # initialize merged list
        merged = []

        # iterate through intervals
        for interval in intervals:
            # if merged is empty or no overlap, add the interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # merge the interval at the point of the highest value
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(Solution().merge(intervals))
