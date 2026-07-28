class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = 0

        def dfs(node):
            nonlocal d
            if not node:
                return 0 

            left = dfs(node.left)
            right = dfs(node.right)

            d = max(d, left + right)
            return max(left, right) + 1 

        dfs(root)
        return d