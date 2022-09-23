# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        curr,prev=head,dummy
        num=-100
        
        while curr:

            num=curr.val
            while(curr.next and num == curr.next.val):
                curr=curr.next
                if(curr.next !=num):
                    prev.next=curr.next
                    curr=prev           
            prev=curr     
            curr=curr.next 
        return (dummy.next)
