# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        negative_inf = float('-inf')

        def dfs(node, max_val):
            if not node:
                return 0

            if node.val >= max_val:
                is_good = 1
            else:
                is_good = 0
            max_val = max(node.val, max_val)
            
            return is_good + dfs(node.left, max_val) + dfs(node.right, max_val)

        return dfs(root, negative_inf)