'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.
'''


class Solution:
    def topKFrequent(nums, k):
        my_dic = {}
        my_dic2 = {}
        arr = []
        arr2 = []
        for i in nums:
            if i not in my_dic:
                my_dic[i] = (1)
            else:
                d = my_dic[i]
                d += 1
                my_dic[i] = (d)
        arr = list(my_dic.values())
        print(my_dic)
        for i in my_dic:
            print(i)
            my_dic2[my_dic[i]] = i
        # print(my_dic2)
        for i in range(0, len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] > arr[j]:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
        for i in range(len(arr)-1, len(arr)-k-1, -1):
            arr2.append(my_dic2[arr[i]])
        print(my_dic2)
        return arr2


nums = [3, 3, 3, 4, 4, 5, 6, 6, 6, 6, 6, 7, 7, 2, 2]
k = 4


print(Solution.topKFrequent(nums, k))
