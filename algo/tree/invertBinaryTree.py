def invertBinaryTree(tree):
    if tree == None:
        return
    swapChildren(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)
    

def swapChildren(node):
    left = node.left
    node.left =node.right
    node.right = left
