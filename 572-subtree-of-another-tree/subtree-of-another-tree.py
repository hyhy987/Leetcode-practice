# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 1. Need to identify the where is the head of the subRoot in the tree
        def sameTree(node1, node2):
            if not node1 and not node2:
                return 0
            if not node1 or not node2:
                return 1

            if node1.val == node2.val:
                val = 0
            else:
                val = 1

            left = sameTree(node1.left, node2.left)
            right = sameTree(node1.right, node2.right)
            
            return left + right + val 

        def dfs(node1, node2):
            if not node1:
                return False
            if sameTree(node1, node2) == 0:
                return True
            else:
                return dfs(node1.left, node2) or dfs(node1.right, node2)
        
        return dfs(root, subRoot)

            
            
            