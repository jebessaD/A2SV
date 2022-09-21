# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack=[]
        output={}
        while head:
            
            output[head]=0
            while (stack and head.val>stack[-1].val):
                output[stack[-1]]=head.val
                a=stack.pop()
            stack.append(head)
            head=head.next
        return list(output.values())
        