# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1
        ptr2 = list2
        if not ptr1:
            return ptr2
        if not ptr2:
            return ptr1
        
        if ptr1.val < ptr2.val:
            ptr1.next = self.mergeTwoLists(ptr1.next, ptr2)
            return ptr1
        else:
            ptr2.next = self.mergeTwoLists(ptr1, ptr2.next)
            return ptr2
