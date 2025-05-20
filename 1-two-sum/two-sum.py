class Solution(object):
    def twoSum(self, nums, target):
        mydict = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in mydict:
                return [mydict[complement], index]
            mydict[value] = index
        return[]
