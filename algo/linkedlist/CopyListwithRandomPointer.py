class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        c = head
        while c is not None:
            cloned = ListNode(c.val)
            cloned.next = c.next
            c.next = cloned
            c = c.next.next
        c = head
        while c is not None:   
            c.next.random = None if c.random is None else c.random.next 
            c = c.next.next
        
        c1 = head
        ch = head.next
        ct = ch
        while c1 is not None:
            c1.next = c1.next.next
            ct.next = ct.next.next
        return ch



head= ListNode()