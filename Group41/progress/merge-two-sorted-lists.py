# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        merged = ListNode()
        ptr = merged
        while curr1 and curr2:
            if  curr1.val < curr2.val:
                ptr.next = ListNode(curr1.val)
                curr1 = curr1.next
                ptr = ptr.next
            else:
                ptr.next = ListNode(curr2.val)
                curr2 = curr2.next
                ptr = ptr.next

        if curr2:
            ptr.next = curr2
        if curr1:
            ptr.next = curr1

        return merged.next