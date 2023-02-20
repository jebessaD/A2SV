# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        ptr = dummy
        curr = head
        index = 0
        if not head:
            return head

        while curr and curr.next:
            if index %2 == 0:
                even_val = curr.next.val
                curr.next = curr.next.next
            else:
                ptr.next = ListNode(even_val)
                ptr = ptr.next
                curr = curr.next
            index += 1

        if index%2 == 1:
            ptr.next = ListNode(even_val)
        curr.next = dummy.next
        
        return head