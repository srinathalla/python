
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def inorderSuccessor(self, target: 'Node') -> 'Node':

        self.prev = None

        def inorder(node):
            if node is None:
                return None

            left = inorder(node.left)
            if left:
                return left

            if self.prev is not None and self.prev == target:
                return node

            self.prev = node
            return inorder(node.right)

        return inorder(target)


root = Node(2)
root.left = Node(1)
root.right = Node(3)

s = Solution()
suc = s.inorderSuccessor(root.left)
print(suc)
