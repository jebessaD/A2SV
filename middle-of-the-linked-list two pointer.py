# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # return head.next.next
        left,right=head,head 
        while right and right.next:
            right=right.next.next
            left=left.next
        return left
