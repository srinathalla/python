class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    maxLength = float('-inf')

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0

        self.diameter(root)
        return self.maxLength - 1

    def diameter(self, node: TreeNode) -> int:

        if node is None:
            return 0

        lLength = self.diameter(node.left)
        rLength = self.diameter(node.right)

        self.maxLength = max(self.maxLength, lLength + rLength + 1)

        return max(lLength, rLength) + 1


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

s = Solution()
print(s.diameterOfBinaryTree(root))
