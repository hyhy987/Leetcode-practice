class Solution(object):
    def minWindow(self, s, t):
        tdict = dict()
        window = dict() 
        res, resLen = [-1,-1], float("infinity")
        l = 0

        if len(t) > len(s):
            return ""

        for i in range(len(t)):
            if t[i] in tdict:
                tdict[t[i]] += 1
            else:
                tdict[t[i]] = 1

        have, need = 0, len(tdict)

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in tdict and window[c] == tdict[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                
                window[s[l]] -= 1
                if s[l] in tdict and window[s[l]] < tdict[s[l]]:
                    have -= 1
                
                l += 1
        l, r = res
        return s[l: r+1] if resLen != float("infinity") else ""
        