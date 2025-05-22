class Solution(object):
    def maxProfit(self, prices):
        max_diff = 0
        min_elem = 99999
        for elem in prices:
            if (elem - min_elem) > max_diff:
                max_diff = elem - min_elem
            if elem < min_elem:
                min_elem = elem
        return max_diff
            
        