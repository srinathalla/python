class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums = []
    traverse(root, 0, sums)
    return sums


def traverse(node, sum, sums):
    if node is None:
        return

    sum += node.value

    if node.left is None and node.right is None:
        sums.append(sum)
        return

    traverse(node.left, sum, sums)
    traverse(node.right, sum, sums)


root = BinaryTree(10)
root.left = BinaryTree(20)
root.right = BinaryTree(30)

print(branchSums(root))
