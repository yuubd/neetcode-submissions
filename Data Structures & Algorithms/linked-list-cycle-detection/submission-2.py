# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        just need a visited set
        '''
        visited = set()
        idx = 0
        while head != None:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        return False
        