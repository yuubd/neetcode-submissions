# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = l = r = ListNode()
        l.next = r.next = head
        r = r.next

        for _ in range(n):
            r = r.next
        # print(r.val)
        while r:
            r = r.next
            l = l.next
            # print(l.val, r.val)
        if l.next:
            l.next = l.next.next
        return dummy.next
    


    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        tmp = head
        while tmp:
            size += 1
            tmp = tmp.next

        goal = size - n

        idx = 0
        prev, curr = None, head
        while idx < goal:
            prev = curr
            curr = curr.next
            idx += 1

        if prev == None:
            return curr.next
        
        prev.next = curr.next
        return head
    


        