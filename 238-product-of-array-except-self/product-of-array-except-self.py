class Solution(object):
    def productExceptSelf(self, nums):
        postfix = 1
        prefix = 1
        answer = [1] * len(nums) 
        for i in range(len(nums)):
            answer[i] = prefix 
            prefix *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]
        return answer
