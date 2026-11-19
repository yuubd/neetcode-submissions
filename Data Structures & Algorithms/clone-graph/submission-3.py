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

            oldToNew[old] = Node(old.val)

            for neighbor in old.neighbors:
                if neighbor not in oldToNew:
                    oldToNew[neighbor] = Node(neighbor.val)
                    oldNodes.append(neighbor)

        for oldNode, newNode in oldToNew.items():
            if oldNode.neighbors == None:
                continue
            
            newNeighbors = []
            for oldNeighbor in oldNode.neighbors: # neighbors never None
                newNeighbor = oldToNew[oldNeighbor]
                newNeighbors.append(newNeighbor)
            newNode.neighbors = newNeighbors

        return oldToNew[node]