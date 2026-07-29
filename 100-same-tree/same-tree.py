# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(node1, node2):
            if not node1 and not node2:
                return 0
            if not node1 or not node2:
                return 1

            if node1.val == node2.val:
                val = 0 
            else:
                val = 1

            left = dfs(node1.left, node2.left)
            right = dfs(node1.right, node2.right)

            return left + right + val 

        return dfs(p, q) == 0


            