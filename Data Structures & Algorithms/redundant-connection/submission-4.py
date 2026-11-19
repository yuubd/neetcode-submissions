class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        subNodes = defaultdict(list)
        for n1, n2 in edges:
            subNodes[n1].append(n2)
            subNodes[n2].append(n1)
        
        no_cycle_nodes = set()
        curr_path = set()
        def found_cycle(node, parent):
            if node in curr_path:
                return True
            if node in no_cycle_nodes:
                return False
            
            curr_path.add(node)

            for neighbor in subNodes[node]:
                if neighbor == parent:
                    continue

                if found_cycle(neighbor, node):
                    return True
                
                
            curr_path.remove(node)
            no_cycle_nodes.add(node)

            return False
        found_cycle(edges[0][0], -1)
        print(curr_path)
        
        for u, v in reversed(edges):
            if u in curr_path and v in curr_path:
                return [u, v]