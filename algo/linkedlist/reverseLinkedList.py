def reverseLinkedList(head):
    prev = None
    curr = head
    next = None

    while curr != None:
        next = curr.next

        curr.next = prev
        prev= curr
        curr = next

    return prev


