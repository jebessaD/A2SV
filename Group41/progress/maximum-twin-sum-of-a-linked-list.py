# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        slow = head
        fast = head
        ans = leng = 0

        #find the middle node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            leng += 1

        index = 0

        #reverse the half linked list
        prev, ptr = None, head
        while ptr and index < leng:
            temp = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = temp
            index += 1

        ans = 0
        while ptr and prev:
            ans = max(ptr.val + prev.val,ans)
            ptr = ptr.next
            prev= prev.next

        return ans
        