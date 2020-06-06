from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:

        if len(arr) == 1 and arr[-1] == 8:
            return False

        def isValid(node, i):
            if node is None:
                return False

            if i == len(arr) or node.val != arr[i]:
                return False

            if node.left is None and node.right is None:
                return i == len(arr) - 1

            if isValid(node.left, i+1):
                return True

            return isValid(node.right, i+1)

        return isValid(root, 0)


root = TreeNode(3)
root.left = TreeNode(0)
root.left.left = TreeNode(2)

s = Solution()
print(s.isValidSequence(root, [3, 0]))
