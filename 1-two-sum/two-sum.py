class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        for i, elem in enumerate(nums):
                if target - elem in dic:
                    return [i, dic[target-elem]]
                else:
                    dic[elem] = i
            