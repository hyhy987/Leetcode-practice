class Solution(object):
    def isAnagram(self, s, t):
        dict_S = dict()
        dict_T = dict()
        for elem in s:
            if elem in dict_S:
                dict_S[elem] += 1
            else:
                dict_S[elem] = 1
        for elem in t:
            if elem in dict_T:
                dict_T[elem] += 1
            else:
                dict_T[elem] = 1
        return dict_T == dict_S
        