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
                # print("rnode", rnode.val, "tmp2", tmp2.val)
            tmp2.next = None # 8
            tmp1 = lnode.next # 4 6 8 10
            # print("lnode",lnode.val,"tmp1",tmp1.val,"tmp2",tmp2.val,"rnode",rnode.val)
            lnode.next = rnode # 2 10
            rnode.next = tmp1 # 2 10 4 68
            lnode = tmp1
            rnode = tmp1 # 2 10 4 6 8

        return






