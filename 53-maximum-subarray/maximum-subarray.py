class Solution(object):
    def maxSubArray(self, nums):
        maxSub =nums[0]
        currSum = 0

        for elem in nums:
            if currSum < 0:
                currSum = 0
            currSum += elem
            maxSub = max(currSum, maxSub)
        return maxSub