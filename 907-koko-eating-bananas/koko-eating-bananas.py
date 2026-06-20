class Solution(object):
    def minEatingSpeed(self, piles, h):

        def calcHours(k):
            hours = 0
            for elem in piles:
                hours += (elem + k - 1 ) // k
            return hours
            
        maxB = 0
        for pile in piles:
            if pile > maxB:
                maxB = pile
        
        # Binary search
        start, end = 1, maxB

        while start < end:
            mid = start + (end - start) // 2

            if calcHours(mid) <= h:
                end = mid 
            else:
                start = mid + 1

        return end  

                

        