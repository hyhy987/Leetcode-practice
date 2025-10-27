class Solution(object):
    def groupAnagrams(self, strs):
        res = {}
        
        for elem in strs:
            c = [0] * 26
            
            for char in elem:
                pos = ord(char) - ord('a')
                c[pos] += 1

            c = tuple(c)

            if c in res:
                res[c].append(elem)
            else:
                res[c] = [elem]         
        return list(res.values())