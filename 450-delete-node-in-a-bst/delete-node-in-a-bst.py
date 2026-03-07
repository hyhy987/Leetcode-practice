# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        if root == None:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left == None and root.right == None:
                return None
            elif root.left and root.right == None:
                return root.left
            elif root.right and root.left == None:
                return root.right
            else:
                curr_left = root.right
                while curr_left.left:
                    curr_left = curr_left.left
                root.val = curr_left.val
                root.right = self.deleteNode(root.right, curr_left.val)
                return root
        return root

            
        