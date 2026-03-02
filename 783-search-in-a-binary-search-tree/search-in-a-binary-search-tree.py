# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        curr_val = root.val
        curr = root 
        while curr:
            curr_val = curr.val
            if val == curr_val:
                return curr
            elif val <= curr_val:
                curr = curr.left
            else:
                curr = curr.right

        