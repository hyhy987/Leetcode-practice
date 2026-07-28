# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math 

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) > 1:
                return float('inf')
            height = max(left, right) + 1
            return height 
            
        if dfs(root) == float('inf'):
            return False
        return True 
            