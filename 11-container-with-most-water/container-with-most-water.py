class Solution(object):
    def maxArea(self, height):
        left = 0 
        right = len(height) - 1
        vol = 0

        while left < right:
            currVol = min(height[left], height[right]) * (right - left)
            vol = max(vol, currVol)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return vol
