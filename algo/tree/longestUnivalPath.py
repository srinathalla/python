
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:

        if root is None:
            return 0

        self.res = 1
        def dfs(node):

            if node is None:
                return (0, 0)

            if node.left is None and node.right is None:
                return (node.val, 1)

            lv, lc = dfs(node.left)

            rv, rc = dfs(node.right)

            ret = 1 + (lc if node.val == lv else 0) + \
                (rc if node.val == rv else 0)
            self.res = max(self.res, ret)

            return (node.val, 1 + max((lc if node.val == lv else 0), (rc if node.val == rv else 0)))

        dfs(root)
        return self.res - 1


s = Solution()

r = TreeNode(5)
r.left = TreeNode(4)
r.right = TreeNode(5)
r.left.left = TreeNode(1)
r.left.right = TreeNode(1)
r.right.right = TreeNode(5)

print(s.longestUnivaluePath(r))
