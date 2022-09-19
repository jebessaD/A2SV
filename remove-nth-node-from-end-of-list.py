# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr=head
        count=0
        while(ptr):
            count+=1
            ptr=ptr.next

        if(count==n):
            head=head.next
            return head
        i=1
        ptr=head
        while(ptr):
            if(i==count-n):
                temp=ptr.next.next
                ptr.next=None
                ptr.next=temp
            i+=1
            ptr=ptr.next      
        return head
                
                
            