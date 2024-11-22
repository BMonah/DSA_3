
class Solution:
    def maxProfit(self, prices):
        res = 0

        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res


# Input: prices = [10,1,5,6,7,1,7,8]
# Output: 6

# Input: prices = [10,8,7,5,2]
# Output: 0

# loop through length of the array
# get the minimum number and record it starting from the first of the array
# subtract values of prices from the minimum as you loop through
# check if the next value is less than the lowest if so assign it as the lowest

def maxProfit(prices):
    res = 0
    lowest = prices[0]
    for price in prices:
        if price < lowest:
            lowest = price
        res = max(res, price-lowest)
    return res


prices = [10, 8, 7, 5, 2, 4]
pricess = [7, 6, 4, 3, 1, 9]
print(maxProfit(pricess))
