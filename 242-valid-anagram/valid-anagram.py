class Solution(object):
    def isAnagram(self, s, t):
        s_dict = {}
        t_dict = {}
        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1
        for char in t:
            if char in t_dict:
                t_dict[char] += 1
            else:
                t_dict[char] = 1
        return s_dict == t_dict

        