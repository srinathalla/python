from collections import deque 

#
# T.C : O(v) v is no of vertices.
# #
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):   
        q = deque()
        q.append(self)

        while len(q) > 0:
            node = q.popleft()
            array.append(node.name)
            for child in node.children:
                q.append(child)
        return array

test1 = Node("A")
test1.addChild("B").addChild("C")
test1.children[0].addChild("D")

print(test1.breadthFirstSearch([]))
        