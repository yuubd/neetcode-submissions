"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # create copies and attach in between
        if head is None:
            return None

        curr = head
        while curr != None:
            newNode = Node(curr.val, curr.next)
            newNode.next = curr.next
            curr.next = newNode
            curr = newNode.next
        # return head

        curr = head
        while curr != None:
            currRandom = curr.random
            if currRandom != None:
                newNode = curr.next
                newNode.random = currRandom.next 
            curr = curr.next.next
        # return head
        res = head.next # the A'
        curr = head
        while curr != None:
            newNode = curr.next
            curr.next = newNode.next
            if newNode.next != None:
                newNode.next = newNode.next.next
            curr = curr.next

        return res
        

    
    
    
    def copyRandomList2(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {}
        oldNode = head
        while oldNode != None:
            oldToNew[oldNode] = Node(oldNode.val)
            oldNode = oldNode.next
        
        res = n = Node(0)   
        oldNode = head
        while oldNode != None:
            newNode = oldToNew[oldNode]
            newNode.next = oldToNew[oldNode.next] if oldNode.next != None else None
            newNode.random = oldToNew[oldNode.random] if oldNode.random != None else None
            n.next = newNode
            n = n.next
            oldNode = oldNode.next

        return res.next
        
        