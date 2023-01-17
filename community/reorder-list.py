# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        ptr,count=head,0
        while ptr:   #count total length
            count+=1
            ptr=ptr.next
        
        prev,curr=None,head
        for i in range(math.ceil(count/2)): #find half
            prev=curr
            curr=curr.next
        prev.next=None
        
        c,rev=curr,None
        while c: #reverse half
            temp=c.next
            c.next=rev
            rev=c
            c=temp        
        p=head
        while p and rev:  # rebuild linked list
            t=p.next
            a=ListNode(rev.val)
            p.next=a
            p.next.next=t
            p=p.next.next
            rev=rev.next