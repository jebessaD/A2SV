# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head 
        length = 0
        while curr:
            curr = curr.next
            length += 1

        limit = length - n - 1
        index = 0
        ptr = head
        if limit == -1:
            return ptr.next
        
        while ptr: 
            if index == limit:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next

            index += 1

        return head