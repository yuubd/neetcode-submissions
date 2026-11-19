# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        if lists is empty then return []

        use min heap and enter the nodes in the list

        Two ways
        1. pop from the heap and append to res, go to the next node, and append to the heap again
        2. add all nodes first? then append to res until there is None in the heap.

        If nodes cant be inserted to the heap, then create a [val of the node, node]

        state
            heap
        
        plan
            scan lists and hpush(node.val, i, node)

            while heap is not empty:
                pop min node
                append the min node to resNode
                create another tuple from the next node
                append to heap
                if None, continue
            ret resNode
        '''

        # if len(lists) == 0 or len(lists) == 0:
        #     return None

        h = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(h, (node.val, i, node))
        
        resNode = dummy = ListNode()
        while h:
            (_, i, minNode) = heapq.heappop(h)
            dummy.next = minNode
            nextNode = minNode.next
            if nextNode != None:
                heapq.heappush(h, (nextNode.val, i, nextNode))
            dummy = dummy.next

        return resNode.next












        