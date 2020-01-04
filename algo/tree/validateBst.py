# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


prev = None


def validateBst(tree):
    global prev
    if tree is None:
        return True

    if validateBst(tree.left) == False:
        return False

    if prev is not None and prev.value > tree.value:
        return False

    return validateBst(tree.right)
