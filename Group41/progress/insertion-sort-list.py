# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        self.head = dummy

        def insertToPosition(ptr):
            curr = self.head
            
            while curr and curr.next:
                if curr.next.val > ptr:
                    temp = curr.next
                    inserted = ListNode(ptr)
                    inserted.next = temp
                    curr.next = inserted
                    break
                curr = curr.next

        def findDecreasing():
            ptr = self.head
            while ptr and ptr.next:
                if ptr.val > ptr.next.val:
                    temp = ptr.next
                    ptr.next = ptr.next.next
                    insertToPosition(temp.val)
                    ptr = self.head
                    
                ptr = ptr.next

        findDecreasing()
        return self.head.next
            

        