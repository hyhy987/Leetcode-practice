class Solution(object):
    def checkInclusion(self, s1, s2):

        if len(s1) > len(s2):
            return False

        hashMap1 = {}
        hashMap2 = {}
        windowLen = len(s1)
        l, r = 0, len(s1) - 1

        # Build hashMap of characters freq in s1
        for c in s1:
            hashMap1[c] = 1 + hashMap1.get(c, 0)

        # Build hashMap for first window in s2:
        for i in range(r + 1):
            hashMap2[s2[i]] = 1 + hashMap2.get(s2[i], 0)

        # Move sliding window along s2
        while r < len(s2):

            # Check if current window has same hashMap as s1
            if hashMap2 == hashMap1:
                return True
            else:
                hashMap2[s2[l]] -= 1
                if hashMap2[s2[l]] == 0:
                    del hashMap2[s2[l]]

                l += 1

                if r + 1 < len(s2):
                    r += 1
                    hashMap2[s2[r]] = 1 + hashMap2.get(s2[r], 0)
                else: 
                    r += 1
        return False
