# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr,prev = head, None
        index = 1
        dummy = ListNode()
        ptr = dummy

        while index < left and curr:
            ptr.next = ListNode(curr.val)
            ptr = ptr.next
            curr = curr.next
            index += 1

        ptr2 = curr
        while curr and index <= right:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            index += 1

        ptr.next = prev        
        ptr2.next = curr
        return dummy.next