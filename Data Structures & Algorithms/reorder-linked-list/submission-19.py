# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None or head.next == None:
            return
        start = head
        mid = head
        end = head
        res = n = ListNode()

        # find the mid
        fast = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            mid = mid.next
        # print(mid.val)
        
        # reverse the mid to end
        end = mid
        prev = None
        while end != None:
            tmp = end.next
            end.next = prev
            prev = end
            end = tmp
        end = prev
        print(end.val)

        # print("mid", mid.val)
        while start != mid and end != None:
            n.next = start
            start = start.next
            n = n.next
            n.next = end
            end = end.next
            n = n.next
            
            

        # print(res.val)
        return 
