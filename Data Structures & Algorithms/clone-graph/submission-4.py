"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None: 
            return None
        
        oldToNew = {}
        oldNodes = deque([node])
        while len(oldNodes) > 0:
            old = oldNodes.popleft()
            if old == None:
                continue
            if old not in oldToNew:
                oldToNew[old] = Node(old.val)
            new = oldToNew[old]
            for neighbor in old.neighbors:
                if neighbor not in oldToNew:
                    oldToNew[neighbor] = Node(neighbor.val)
                    oldNodes.append(neighbor)
                new.neighbors.append(oldToNew[neighbor])

        return oldToNew[node]