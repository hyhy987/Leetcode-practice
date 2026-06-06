class Solution(object):
    def characterReplacement(self, s, k):
        hashMap = dict()
        l = 0
        res = 0

        for r in range(len(s)):
            
            if s[r] not in hashMap:
                hashMap[s[r]] = 1
            else:
                hashMap[s[r]] += 1

            windowLen = r - l + 1

            maxCount = 0
            for _, count in hashMap.items():
                if count > maxCount:
                    maxCount = count
            
            if windowLen - maxCount <= k:
                res = max(windowLen, res)

            else:
                while windowLen - maxCount > k:
                    hashMap[s[l]] -= 1
                    l += 1
                    maxCount = 0
                    windowLen -= 1
                    for count in hashMap.values():
                        if count > maxCount:
                            maxCount = count
        return res
