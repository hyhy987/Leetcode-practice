# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        if root == None:
            root = TreeNode(val)
            return root
        def insertNode(node, val):
            if val <= node.val:
                if node.left != None:
                    insertNode(node.left, val)
                if node.left == None:
                    node.left = TreeNode(val)
            elif val > node.val:
                if node.right != None:
                    insertNode(node.right, val)
                if node.right == None:
                    node.right = TreeNode(val)
            else:
                return 
        insertNode(root, val)
        return root