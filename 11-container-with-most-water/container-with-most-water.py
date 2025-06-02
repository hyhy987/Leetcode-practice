class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        base = len(height) - 1
        maxArea = 0

        for i in range (len(height)):
            newArea = min(height[l], height[r]) * (r-l)
            if newArea > maxArea:
                maxArea = newArea

            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
        return maxArea
            
        