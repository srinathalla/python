class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def minCameraCover(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        def postOrder(root):
            if root is None:
                return 2

            l = postOrder(root.left)
            r = postOrder(root.right)

            if l == 2 and r == 2:
                return 0

            if l == 0 or r == 0:
                self.c += 1
                return 1

            if l == 1 or r == 1:
                return 2

        self.c = 0
        res = postOrder(root)
        return self.c + (1 if res == 0 else 0)


root = TreeNode(0)
root.left = TreeNode(0)
root.left.left = TreeNode(0)
root.left.right = TreeNode(0)

s = Solution()
print(s.minCameraCover(root))
