class Solution(object):
    def lengthOfLongestSubstring(self, s):
        mySet = set()
        l = 0
        maxLength = 0

        for r in range(len(s)):
            while s[r] in mySet:
                mySet.remove(s[l])
                l += 1
            mySet.add(s[r])
            maxLength = max(maxLength, r - l + 1)
        return maxLength