class Solution(object):
    def generateParenthesis(self, n):
        
        res = [] 
        current = ""

        def recursiveCombi(combi, numOpen, numClose, curr):
            if numOpen == 0 and numClose == 0:
                res.append(curr)  
                return

            if numOpen > 0:
                newCurr = curr + "("
                recursiveCombi(combi, numOpen - 1, numClose, newCurr)
            
            if numClose > numOpen:
                newCurr = curr + ")"
                recursiveCombi(combi, numOpen, numClose - 1, newCurr)

            return combi
        return recursiveCombi(res, n, n, "")