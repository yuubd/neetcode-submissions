# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        1. save the l node.next to a tmp 1
        2. r node go to the end.
        3. save the prev of the r node in tmp 2 and tmp2.next = None
        4. lnode.next=rnode
        5. rnode.next = tmp 1
        6. update lnode = rnode 
        repeat until l is None
        '''

        lnode = head
        rnode = head
        tmp1 = lnode.next
        tmp2 = None
        while tmp1 != None:
            while rnode.next != None:
                tmp2 = rnode 
                rnode = rnode.next
            tmp2.next = None
            tmp1 = lnode.next
            lnode.next = rnode
            rnode.next = tmp1
            lnode = tmp1
            rnode = tmp1

        return






