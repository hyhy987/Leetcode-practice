class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        max_count = 0
        for elem in num_set:
            count = 0
            if elem - 1 in num_set:
                continue
            count += 1
            temp = elem
            while temp + 1 in num_set:
                temp += 1
                count += 1
            if count > max_count:
                max_count = count
        return max_count
        