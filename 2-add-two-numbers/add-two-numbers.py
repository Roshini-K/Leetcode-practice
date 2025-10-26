# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        tail=dummy
        carry=0

        while l1 or l2 or carry:
            val1=l1.val if l1 is not None else 0
            val2=l2.val if l2 is not None else 0
    
            summ=val1+val2+carry
            digit=summ%10
            carry=summ//10

            newNode=ListNode(digit)
            tail.next=newNode
            tail=tail.next

            l1=l1.next if l1 is not None else None
            l2=l2.next if l2 is not None else None

        result=dummy.next
        return result


        