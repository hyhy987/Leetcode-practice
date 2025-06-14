# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        def invert(node):
            if node is None:
                return 
            if node.left is None and node.right is None:
                return node
            else:
                temp = node.left
                node.left = node.right
                node.right = temp

                invert(node.left)
                invert(node.right)
        invert(root)

        return root