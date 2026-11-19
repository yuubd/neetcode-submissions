# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = n = ListNode()

        prev = n
        carryOver = 0
        while l1 != None or l2!= None or carryOver > 0:
            l1Val = l1.val if l1 != None else 0
            l2Val = l2.val if l2 != None else 0
            
            sumNodes = l1Val + l2Val + carryOver
            carryOver = 1 if sumNodes >= 10 else 0
            digit = sumNodes % 10


            n.next = ListNode(digit)
            n = n.next
            
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None

        

        return res.next


