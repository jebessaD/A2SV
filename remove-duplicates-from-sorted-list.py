# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr=head
        prev=None
        num=-101

        while(ptr):
            if(ptr.val==num):
                prev.next=ptr.next
                ptr.val=None
                ptr=ptr.next  
            else:
                prev=ptr
                num=prev.val
                ptr=ptr.next
        return head