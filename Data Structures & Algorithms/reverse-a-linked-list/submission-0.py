# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        [] => []
        if curr = null, return prev
        
        [1] => [1]
        if curr = null, it s the end return prev

        [1,2] => [2,1]
        if curr is not null, store the curr.next to tmp_node, curr.next = prev
        curr = 1
        tmp = 2
        curr.next = prev (null)

        curr = tmp
        '''

        prev = None
        curr = head
        while curr != None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        return prev


        



