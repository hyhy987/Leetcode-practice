# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []

        stack = [(root, False, [root.val])]
        res = []

        while len(stack) != 0:
            node, visited, path = stack.pop()

            if visited == True:
                if node.right is None and node.left is None:
                    if sum(path) == targetSum:
                        res.append(path)
            
            else:
                stack.append((node, True, path))

                if node.right is not None:
                    stack.append((node.right, False, path + [node.right.val]))
                
                if node.left is not None:
                    stack.append((node.left, False, path + [node.left.val]))

        return res 