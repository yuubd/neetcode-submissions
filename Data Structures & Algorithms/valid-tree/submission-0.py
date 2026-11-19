class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nToNodes = defaultdict(list)
        visited = set()
        
        for i in range(n):
            nToNodes[i] = []
        for n1, n2 in edges:
            nToNodes[n1].append(n2)
            nToNodes[n2].append(n1)

        def invalid_tree_node(n, parent):
            if n in visited: # whenever here there is a cycle
                return True
            # if nToNodes == []: # separated node. Dont need it. The last chekc covers it
            #     return False
            visited.add(n)

            for nextN in nToNodes[n]:
                if nextN == parent:
                    continue
                if invalid_tree_node(nextN, n):
                    return True # invalid tree
            return False
        
        if invalid_tree_node(0, -1):
            return False
        
        return len(visited) == n
            
                

