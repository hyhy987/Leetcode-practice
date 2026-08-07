# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        def dfs(node, maxV):
            if not node:
                return 0
            if maxV > node.val:
                val = 0
            else:
                val = 1

            if node.val > maxV:
                nextMax = node.val
            else:
                nextMax = maxV
            left = dfs(node.left, nextMax) if node.left else 0
            right = dfs(node.right, nextMax) if node.right else 0
            return val + left + right 
        return dfs(root, root.val)
            