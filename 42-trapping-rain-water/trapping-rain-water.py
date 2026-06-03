class Solution(object):
    def trap(self, height):
        maxLeft = height[0]
        maxRight = height[len(height) - 1]
        l, r = 0, len(height) - 1
        volume = 0
        while l < r:
            if maxLeft <= maxRight:
                l += 1
                volume += max(min(maxLeft, maxRight) - height[l], 0)
                maxLeft = max(maxLeft, height[l])

            else:
                r -= 1
                volume += max(min(maxLeft, maxRight) - height[r], 0)
                maxRight = max(maxRight, height[r])

        return volume

            
        