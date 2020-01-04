# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes


def removeKthNodeFromEnd(head, k):   
    fast = head
    slow = head
    while k > 0 and fast != None:
        fast = fast.next
        k -=1
    
    if fast is None:
        head.value = head.next.value
        head.next = head.next.next
        return 
    
    while fast.next != None:
         fast = fast.next
         slow = slow.next
    
    slow.next = slow.next.next

test10 = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
removeKthNodeFromEnd(test10, 10)
print(test10.getNodesInArray())

