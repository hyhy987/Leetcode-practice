class Solution(object):
    def isValid(self, s):
        mystack = []
        chars = {'[': ']', '{': '}', '(': ')'}

        for char in s:
            if char in chars:
                mystack.append(char)
            else:
                if mystack == []:
                    return False
                if chars[mystack.pop()] != char:
                    return False
        return mystack == []
        