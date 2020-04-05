# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        stack, i = [], 0

        while i < len(S):
            level = 0
            val = 0

            while i < len(S) and S[i] == '-':
                level, i = level + 1, i + 1

            while i < len(S) and S[i] != '-':
                val = val * 10 + int(S[i])
                i += 1

            while len(stack) > level:
                stack.pop()

            node = TreeNode(val)
            if stack and stack[-1].left is None:
                stack[-1].left = node
            elif stack and stack[-1].right is None:
                stack[-1].right = node

            stack.append(node)

        return stack[0]


s = Solution()
print(s.recoverFromPreorder("1-2--3--4-5--6--7").val)
