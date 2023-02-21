# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = l1
        ptr2 = l2
        carry = 0
        dummy = ListNode()
        curr = dummy
        while ptr1 and ptr2:
            summation = ptr1.val + ptr2.val + carry
            unit_digit = summation % 10
            curr.next = ListNode(unit_digit)
            curr = curr.next
            carry = summation // 10
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        new_ptr = ptr1 or ptr2
        while new_ptr:
            summation = new_ptr.val + carry
            unit_digit = summation % 10
            curr.next = ListNode(unit_digit)
            curr = curr.next
            carry = summation // 10
            new_ptr = new_ptr.next

        if carry:
            curr.next = ListNode(carry)

        return dummy.next
