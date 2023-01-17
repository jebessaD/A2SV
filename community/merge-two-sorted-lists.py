# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if(not list1 and not list2):
            return list1
        elif(not list1):
            return list2
        elif(not list2):
            return list1

        head=ListNode()
        ptr=head
        while(list1 or list2):
            if(list1 and list2):
                if (list1.val < list2.val):
                    small=list1
                    list1=list1.next
                else:
                    small=list2
                    list2=list2.next
                
                ptr.next=ListNode(small.val)
                
            elif(list1):
                ptr.next=ListNode(list1.val)
                list1=list1.next
                
            elif(list2):
                ptr.next=ListNode(list2.val)
                list2=list2.next
            ptr=ptr.next
        return head.next 