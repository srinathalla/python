
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:

        q = []
        q.append(root)

        ans = 1
        level = 1
        gsum = root.val

        while q:
            s = len(q)
            ls = 0
            for i in range(s):
                node = q.pop(0)
                ls += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if ls > gsum:
                gsum = ls
                ans = level
            level += 1
        return ans


root = TreeNode(989)
root.right = TreeNode(10250)
root.right.left = TreeNode(98693)
root.right.right = TreeNode(-89388)
root.right.right.right = TreeNode(-32127)
s = Solution()
print(s.maxLevelSum(root))
