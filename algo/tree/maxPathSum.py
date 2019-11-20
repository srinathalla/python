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
