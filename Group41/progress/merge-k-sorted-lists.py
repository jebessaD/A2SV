# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for head in lists:
            while head:
                heappush(heap,head.val)
                head = head.next

        dummy = ListNode(0)
        ptr = dummy
        while heap:
            num = heappop(heap)
            ptr.next = ListNode(num)
            ptr = ptr.next

        return dummy.next

                