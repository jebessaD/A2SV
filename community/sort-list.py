# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr,arr=head,[]
        while ptr:
            arr.append(ptr.val)
            ptr=ptr.next
        arr.sort()
        ptr=head
        for i in range(len(arr)):
            ptr.val=arr[i]
            ptr=ptr.next
            
        return head