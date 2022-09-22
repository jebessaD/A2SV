# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ptr=head
        count=0
        while ptr:
            count+=1
            ptr=ptr.next

        #reverse half
        curr,prev=head,None
        half=0
        while (curr and half <count//2):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr= temp
            half+=1

        ans=curr.val + prev.val
        while(curr and prev):
            ans=max(ans,curr.val + prev.val)
            curr=curr.next
            prev= prev.next
        return ans
