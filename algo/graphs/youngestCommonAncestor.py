# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

    def addAsAncestor(self, descendants):
        for descendant in descendants:
            descendant.ancestor = self

#
# T.C L O(m*n) where m is depth of descendantOne
#                    n is depth of descendatTwo
# #


def getYoungestCommonAncestorNaive(topAncestor, descendantOne, descendantTwo):
    if descendantOne == descendantTwo:
        return descendantOne.ancestor

    if descendantOne.ancestor == descendantTwo:
        return descendantTwo

    if descendantTwo.ancestor == descendantOne:
        return descendantOne

    a1 = descendantOne
    a2 = descendantTwo
    while a1 != None:
        a2 = descendantTwo
        while a2 != None:
            if a2 == a1:
                return a1
            a2 = a2.ancestor
        a1 = a1.ancestor

    return topAncestor

# T.C : O(d) where d is depth of the tree. S.C : O(1)


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depth1 = getDepth(descendantOne)
    depth2 = getDepth(descendantTwo)

    if depth1 > depth2:
        return backTrackTillAncestor(descendantOne, descendantTwo, depth1 - depth2)
    else:
        return backTrackTillAncestor(descendantTwo, descendantOne, depth2 - depth1)


def backTrackTillAncestor(lowerDescedant, higherDescendant, diff):
    while diff > 0:
        lowerDescedant = lowerDescedant.ancestor
        diff -= 1

    while lowerDescedant != higherDescendant:
        lowerDescedant = lowerDescedant.ancestor
        higherDescendant = higherDescendant.ancestor

    return lowerDescedant


def getDepth(node):
    depth = 0
    while node is not None:
        node = node.ancestor
        depth += 1
    return depth


ancestralTrees = {}
ALPHABET = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for letter in ALPHABET:
    ancestralTrees[letter] = AncestralTree(letter)
ancestralTrees["A"].addAsAncestor(
    [
        ancestralTrees["B"],
        ancestralTrees["C"],
        ancestralTrees["D"],
        ancestralTrees["E"],
        ancestralTrees["F"],
    ]
)
ancestralTrees["B"].addAsAncestor(
    [ancestralTrees["G"], ancestralTrees["H"], ancestralTrees["I"]]
)
ancestralTrees["C"].addAsAncestor([ancestralTrees["J"]])
ancestralTrees["D"].addAsAncestor([ancestralTrees["K"], ancestralTrees["L"]])
ancestralTrees["F"].addAsAncestor([ancestralTrees["M"], ancestralTrees["N"]])
ancestralTrees["H"].addAsAncestor(
    [ancestralTrees["O"], ancestralTrees["P"],
        ancestralTrees["Q"], ancestralTrees["R"]]
)
ancestralTrees["K"].addAsAncestor([ancestralTrees["S"]])
ancestralTrees["P"].addAsAncestor([ancestralTrees["T"], ancestralTrees["U"]])
ancestralTrees["R"].addAsAncestor([ancestralTrees["V"]])
ancestralTrees["V"].addAsAncestor(
    [ancestralTrees["W"], ancestralTrees["X"], ancestralTrees["Y"]]
)
ancestralTrees["X"].addAsAncestor([ancestralTrees["Z"]])

# print(getYoungestCommonAncestor(
#    ancestralTrees["A"], ancestralTrees["A"], ancestralTrees["B"]
# ).name)

print(getYoungestCommonAncestor(
    ancestralTrees["A"], ancestralTrees["Z"], ancestralTrees["B"]).name)
