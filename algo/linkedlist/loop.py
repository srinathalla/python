# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

  ##
   # T.C : O(n) where n is length of linkedlist.
   # S.C : O(1)
   # @param {} head
   #


def findLoop(head):
    fast = head.next.next
    slow = head.next

    while fast != slow:
        fast = fast.next.next
        slow = slow.next

    slow = head
    while fast != slow:
        slow = slow.next
        fast = fast.next

    return slow
