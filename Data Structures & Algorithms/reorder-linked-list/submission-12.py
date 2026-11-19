# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        1. find the half
        2. reverse the half
        3. reorder the pointers

        This is possible cuz the direction of the pointers are merging to center,
        so we need a reserve of the second half to the center
        '''

        # 1.
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next if fast.next.next == None else fast.next.next
        print("slow.val", slow.val, "fast.val", fast.val)
        
        # 2.
        prev = None
        curr = slow.next
        slow.next = None
        while curr != None and curr != fast:
            tmp = curr.next 
            curr.next = prev
            prev = curr 
            curr = tmp
        if curr != None:
            curr.next = prev
        

        #3. 
        start = head
        end = curr
        while end != None and start != None:
            tmp = start.next
            start.next = end
            tmp2 = end.next
            end.next = tmp
            start=tmp
            end=tmp2




        
            
            








def reorderListN2(self, head: Optional[ListNode]) -> None:
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






