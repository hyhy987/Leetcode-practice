class Solution(object):
    def containsDuplicate(self, nums):
        mySet = set()
        for elem in nums:
            if elem in mySet:
                return True
            else:
                mySet.add(elem)
        return False