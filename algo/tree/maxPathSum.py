sum = 0


def maxPathSum(tree):
    global sum
    sum = 0
    traverse(tree)
    return sum


def traverse(tree):
    global sum
    if (tree == None):
        return 0

    left = max(0, traverse(tree.left))
    right = max(0, traverse(tree.right))
    sum = max(sum, left + right + tree.value)

    return max(left, right) + tree.value


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    sum = float('-inf')
    def maxPathSum(self, root: TreeNode) -> int:

        self.pathSum(root)
        return self.sum

    def pathSum(self, node: TreeNode) -> int:

        if node is None:
            return 0

        leftSum = max(0, self.pathSum(node.left))
        rightSum = max(0, self.pathSum(node.right))

        self.sum = max(self.sum, leftSum + rightSum + node.val)

        return max(leftSum, rightSum) + node.val


root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

s = Solution()
print(s.maxPathSum(root))
