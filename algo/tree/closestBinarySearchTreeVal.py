# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:

        values = []

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)
        l = 0
        h = len(values)-1
        diff = values[-1] - values[0]
        no = -1
        while l <= h:

            m = l + h >> 1

            if values[m] == target:
                no = values[m]
                break
            elif values[m] < target:
                if target - values[m] < diff:
                    diff = target - values[m]
                    no = values[m]
                l = m + 1
            else:
                if values[m] - target < diff:
                    diff = values[m] - target
                    no = values[m]
                h = m - 1
        return no


s = Solution()

r = TreeNode(4)
r.left = TreeNode(2)
r.left.left = TreeNode(1)
r.left.right = TreeNode(3)
r.right = TreeNode(5)
print(s.closestValue(r, 3.714))
