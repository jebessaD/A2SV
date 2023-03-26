class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        
    def get(self, index: int) -> int:
        curr = self.head
        ind = 0
        while ind < index  and curr:
            curr = curr.next
            ind += 1

        if curr:
            return curr.val
        return - 1

    def addAtHead(self, val: int) -> None:
        new_head = ListNode(val)
        temp = self.head
        new_head.next = temp
        self.head = new_head
  
    def addAtTail(self, val: int) -> None:
        curr = self.head
        if not curr:
            self.head = ListNode(val)
            return

        while curr.next:
            curr = curr.next

        curr.next = ListNode(val)
           

    def addAtIndex(self, index: int, val: int) -> None:
        ind = 0
        curr = self.head
        if index == 0:
            self.addAtHead(val)

        while ind < index - 1 and curr:
            curr = curr.next
            ind += 1

        if curr:
            temp = curr.next
            curr.next = ListNode(val)
            curr = curr.next
            curr.next = temp

    def deleteAtIndex(self, index: int) -> None:
        ind = 0
        curr = self.head
        if index == 0:
            self.head = self.head.next
            return

        while ind < index - 1 and curr and curr.next:
            curr = curr.next
            ind += 1

        if curr.next:
            curr.next = curr.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)