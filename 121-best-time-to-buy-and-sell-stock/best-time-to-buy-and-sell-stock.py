class Solution(object):
    def maxProfit(self, prices):
        l, r = 0, 1
        profit = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                profit = max(prices[r] - prices[l], profit)
                r += 1
        return profit  

        
        