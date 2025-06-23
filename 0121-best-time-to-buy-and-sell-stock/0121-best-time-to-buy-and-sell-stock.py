class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxr = prices[len(prices)-1]
        res = 0
        for i in range(len(prices)-1,-1, -1):
            if prices[i] < maxr:
                res = max(res, maxr-prices[i])
            maxr = max(maxr, prices[i])

        return res


