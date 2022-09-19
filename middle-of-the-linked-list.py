# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # return head.next.next
        left,right=head,head
        
        count=0
        while right:
            right=right.next
            count+=1
        for i in range(count//2):
            left=left.next
            
        return left
