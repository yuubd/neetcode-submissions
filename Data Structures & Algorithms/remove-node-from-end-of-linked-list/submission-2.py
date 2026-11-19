# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        tmp = head
        while tmp:
            size += 1
            tmp = tmp.next
        print(size)

        goal = size - (n % size) if size > n else size - n

        idx = 0
        prev, curr = None, head
        while idx < goal:
            prev = curr
            curr = curr.next
            idx += 1
        print('idx',idx, 'goal',goal)
        if prev == None:
            return curr.next if curr.next else None
        
        prev.next = curr.next if curr else None
        # print('idx', idx, 'prev', prev.val, 'curr', curr.val)
        return head
    


        