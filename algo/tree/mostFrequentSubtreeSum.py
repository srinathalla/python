
from collections import Counter


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:

        c = Counter()

        def recurse(node):
            if node is None:
                return [0]

            l = recurse(node.left)
            r = recurse(node.right)
            s = l + r + node.val
            c[s] += 1

            return s

        hv = max(c.values())
        res = []
        return [k for k, v in c.most_common() if v == hv]


root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(-3)
s = Solution()
s.findFrequentTreeSum(root)
