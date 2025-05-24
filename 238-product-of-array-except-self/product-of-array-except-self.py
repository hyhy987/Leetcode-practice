class Solution(object):
    def productExceptSelf(self, nums):
        result = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)):
            result[-1-i] *= postfix
            postfix *= nums[-1-i]
        return result