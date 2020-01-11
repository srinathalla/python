class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummyHead = ListNode(-1)
        dummyHead.next = head

        fast = dummyHead
        slow = dummyHead

        while n > 0:
            fast = fast.next
            n -= 1

        while fast != None and fast.next != None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummyHead.next


s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

head = s.removeNthFromEnd(head, 2)
print(head)
