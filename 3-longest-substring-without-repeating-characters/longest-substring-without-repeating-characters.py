class Solution(object):
    def lengthOfLongestSubstring(self, s):
        mySet = set()
        l = 0
        substringLength = 0

        for r in range(len(s)):
            while s[r] in mySet:
                mySet.remove(s[l])
                l += 1

            mySet.add(s[r])
            substringLength = max(substringLength, r - l + 1)
        return substringLength