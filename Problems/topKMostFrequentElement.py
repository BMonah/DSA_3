class Solution:
    def topKFrequent(self, arr, k):
        results = [[] for i in range(len(arr)+1)]
        my_map = {}
        final = []
        for index in range(len(arr)):
            my_map[arr[index]] = my_map.get(arr[index], 0) + 1

        for key, value in my_map.items():
            results[value].append(key)

        for values in range(len(results)-1, 0, -1):
            for items in results[values]:
                final.append(items)
                if len(final) == k:
                    return final


print(Solution().topKFrequent([1, 2, 2, 3, 3, 34, 5], 2))


class Solution:
    def topKFrequent(nums, k):
        results = [[] for i in range(len(nums)+1)]
        my_dic = {}
        final = []
        for index in range(len(nums)):
            my_dic[nums[index]] = my_dic.get(nums[index], 0) + 1
        for key, value in my_dic.items():
            results[value].append(key)
        for items in range(len(results)-1, 0, -1):
            for values in results[items]:
                final.append(values)
                if len(final) == k:
                    return final


print(Solution.topKFrequent([1, 2, 2, 3], 2))
