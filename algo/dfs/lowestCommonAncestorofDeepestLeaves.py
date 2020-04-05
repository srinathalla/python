# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root

        def helper(node):
            if node is None:
                return 0, None

            h1, l = helper(node.left)
            h2, r = helper(node.right)

            if h1 > h2:
                return h1 + 1, l
            elif h1 < h2:
                return h2 + 1, r
            else:
                return h1 + 1, node

        return helper(root)[1]


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

s = Solution()
lca = s.lcaDeepestLeaves(root)
print(lca.val)
