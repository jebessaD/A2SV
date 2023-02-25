# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ptr = head
        leng = 0
        if not ptr:
            return head

        while ptr:
            ptr = ptr.next
            leng += 1

        k = k % leng
        limit = leng - k - 1
        if k == 0:
            return head

        curr = head
        ind = 0
        while curr and ind < limit:
            curr = curr.next
            ind += 1

        reversed_head = curr.next
        curr.next = None
        new_ptr = reversed_head
        while new_ptr and new_ptr.next:
            new_ptr = new_ptr.next
        new_ptr.next = head
        return reversed_head
   