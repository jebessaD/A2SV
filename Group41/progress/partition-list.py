# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        new_head = ListNode()
        curr = new_head
        ptr = head
        while ptr:
            if  ptr.val < x:
                curr.next = ListNode(ptr.val,None)
                curr = curr.next
            ptr = ptr.next

        ptr = head
        while ptr:
            if  ptr.val >= x:
                curr.next = ListNode(ptr.val,None)
                curr = curr.next
            ptr = ptr.next
        
        return new_head.next