# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans = {}
        curr = head
        stack = []
        while curr:
            ans[curr] = 0
            while stack and stack[-1].val < curr.val:
                ans[stack[-1]] = curr.val
                num = stack.pop()

            stack.append(curr)
            curr = curr.next
        return ans.values()