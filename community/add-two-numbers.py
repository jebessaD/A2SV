# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1,ptr2=l1,l2
        summation=ListNode()
        curr=summation
        rem=0
        while(ptr1 or ptr2):
            if(ptr1 and ptr2):
                curr.next=ListNode((ptr1.val + ptr2.val +rem)%10)
                rem=int((ptr1.val + ptr2.val + rem)/10 )
                ptr1=ptr1.next
                ptr2=ptr2.next
                curr=curr.next
                if(rem>0 and not ptr1 and not ptr2):
                    curr.next=ListNode(rem)
                    curr=curr.next
            elif(ptr1):
                curr.next=ListNode((ptr1.val+rem)%10)
                rem=(ptr1.val+rem)//10 
                ptr1=ptr1.next
                curr=curr.next
                if(rem>0 and not ptr1):
                    curr.next=ListNode(rem%10)
                    curr=curr.next
            elif(ptr2):
                curr.next=ListNode((ptr2.val+rem)%10)
                rem=(ptr2.val+rem)//10 
                ptr2=ptr2.next
                curr=curr.next
                if(rem>0 and not ptr2):
                    curr.next=ListNode(rem)
                    # rem=(rem)
                    curr=curr.next
                
        return summation.next