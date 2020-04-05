
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':

        def flat(node):
            curr = node
            while curr.next is not None:
                if curr.child is not None:
                    f = flat(curr.child)
                    f[0].prev = curr
                    f[1].next = curr.next
                    curr.next.prev = f[1]
                    curr.next = f[0]
                    curr.child = None
                    curr = f[1]
                curr = curr.next

            return (head, curr)
        return flat(head)[0]


s = Solution()

head = Node(3, None, None, None)
head.child = Node(7, None, None, None)
head.child.next = Node(8, None, None, None)
head.next = Node(4, None, None, None)

f = s.flatten(head)
print(f)
