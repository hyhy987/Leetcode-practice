class Solution(object):
    def containsDuplicate(self, nums):
        myset = set(())
        for elem in nums:
            if elem in myset:
                return True
            myset.add(elem)
        return False
        