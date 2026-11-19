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
        
        