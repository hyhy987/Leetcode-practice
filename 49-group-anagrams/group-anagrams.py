class Solution(object):
    def groupAnagrams(self, strs):
        res = []
        mydict = {}

        for elem in strs:
            if ''.join(sorted(elem)) in mydict:
                mydict[''.join(sorted(elem))].append(elem)
            else:
                mydict[''.join(sorted(elem))] = [elem]
        for elem in mydict.values():
            res.append(elem)
        
        return res