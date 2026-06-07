class Solution(object):
    def minWindow(self, s, t):
        if t == "":
            return ""
        hashT = {}
        hashS = {}
        l, r = 0, 0
        res, resLen = [-1, -1], float('inf')
        

        # Build hashMap for t first
        for c in t:
            hashT[c] = 1 + hashT.get(c, 0)

        have, need = 0, len(hashT)

        # Sliding window
        for r in range(len(s)):
            c = s[r]
            hashS[c] = 1 + hashS.get(c, 0)

            if c in hashT and hashS[c] == hashT[c]:
                have += 1

            while have == need:
                # Update result
                if (r - l + 1 ) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                hashS[s[l]] -= 1

                if s[l] in hashT and hashS[s[l]] < hashT[s[l]]:
                    have -= 1
                l += 1
                
        if resLen != float("inf"):
            return s[res[0]: res[1] + 1]
        else:
            return ""            