class Solution(object):
    def threeSum(self, nums):
        nums = sorted(nums)
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            num = nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if num + nums[left] + nums[right] == 0:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                    
                elif num + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        
        return res 