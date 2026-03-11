# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if root == None:
            return 0
        def bfs(node):
            if node == None:
                return
            l_count = 0
            r_count = 0
            if node.left:
                l_count = bfs(node.left) + 1
            if node.right:
                r_count = bfs(node.right) + 1
            max_count = max(l_count, r_count)
            return max_count 
        count = bfs(root) + 1
        return count 