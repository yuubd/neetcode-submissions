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
            
            strSum = str(l1Val + l2Val + carryOver)
            listSum = [int(c) for c in strSum]
            digit = listSum[1] if len(listSum) > 1 else listSum[0]
            carryOver = listSum[0] if len(listSum) > 1 else 0
            print(digit)
            n.next = ListNode(digit)
            n = n.next
            prev.next = n
            prev = n
            print('listSum', listSum)
            
            
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None

        

        return res.next


