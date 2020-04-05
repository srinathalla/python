
from collections import defaultdict
from typing import List
import bisect


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:

        if root is None:
            return

        g = defaultdict(set)

        def dfs(node, g):

            if node is None:
                return

            if node.left:
                g[node.val].add(node.left.val)
                g[node.left.val].add(node.val)

            if node.right:
                g[node.val].add(node.right.val)
                g[node.right.val].add(node.val)

            dfs(node.left, g)
            dfs(node.right, g)

        dfs(root, g)

        q = []
        q.append(target)
        visited = set()
        visited.add(target)

        dist = 0
        res = []
        while q:
            size = len(q)
            for i in range(size):
                if dist < K:
                    v = q.pop(0)

                    for av in g[v]:
                        if av not in visited:
                            visited.add(av)
                            q.append(av)
                else:
                    res.append(q.pop(0))
            dist += 1

        return res


print(bisect.bisect([2, 3], 1))
s = Solution()
print(s.distanceK(TreeNode(1), 1, 0))


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

print(s.distanceK(root, 5, 2))
