# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverseList(head):
            prev,curr=None,head
            while curr:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            return prev
        
        l1,l2 = reverseList(l1),reverseList(l2)
        temp=0
        ans=ListNode()
        ptr=ans
        while(l1 or l2 or temp):
            if l1:
                temp +=l1.val
                l1=l1.next
            if l2:
                temp +=l2.val
                l2=l2.next
            
            ptr.next=ListNode(temp%10)
            ptr=ptr.next
            temp//=10
        
        return reverseList(ans.next)
            
                
                
        