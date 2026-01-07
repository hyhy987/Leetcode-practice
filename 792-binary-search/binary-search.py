class Solution(object):
    def search(self, nums, target):
        begin = 0
        end = len(nums) - 1
        while begin < end:
            mid = begin + (end - begin) / 2
            if target <= nums[mid]:
                end = mid
            else:
                begin = mid + 1
        if nums[end] == target:
            return end
        else:
            return -1
        