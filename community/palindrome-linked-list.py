# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev,curr,ptr=None,head,head
        count=0
        while(ptr):
            count+=1
            ptr=ptr.next
        if(count==1):
            return True
        c=1
        while curr and c<=count//2 :
            c+=1
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        if(count%2!=0):
            curr=curr.next
            
        while(curr):
            if(curr.val==prev.val):
                prev=prev.next
                curr=curr.next
            else:
                return False
        return True
        