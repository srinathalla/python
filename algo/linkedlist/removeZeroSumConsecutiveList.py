# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:

        dummy = ListNode(-1)
        dummy.next = head

        map = {}
        map[0] = dummy

        s = 0
        curr = head
        while curr is not None:
            s += curr.val
            if s in map:
                prev = map[s].next
                ps = s
                while prev != curr:
                    ps += prev.val
                    del map[ps]
                    prev = prev.next
                map[s].next = curr.next
            else:
                map[s] = curr
            curr = curr.next

        return dummy.next
