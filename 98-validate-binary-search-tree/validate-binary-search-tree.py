from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = deque()
        currMax = float("-inf")
        curr = root 

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop() 
            if curr.val <= currMax:
                return False 
            currMax = curr.val
            curr = curr.right 
                
        return True
