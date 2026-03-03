# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        prev = [float('-inf')]
        
        def dfs(node):
            if node == None:
                return True
            if not dfs(node.left):
                return False
            if node.val <= prev[0]:
                return False

            prev[0] = node.val
            
            return dfs(node.right)
    
        return dfs(root)
        