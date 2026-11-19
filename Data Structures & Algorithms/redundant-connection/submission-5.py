class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        subNodes = defaultdict(list)
        for n1, n2 in edges:
            subNodes[n1].append(n2)
            subNodes[n2].append(n1)
        
        visited = set()
        cycle_nodes = set()
        cycle_start_node = -1
        def found_cycle(node, parent):
            nonlocal cycle_start_node
            if node in visited:
                cycle_start_node = node
                return True
            visited.add(node)

            for neighbor in subNodes[node]:
                if neighbor == parent:
                    continue
                if found_cycle(neighbor, node):
                    if cycle_start_node != -1:
                        cycle_nodes.add(node)
                    if cycle_start_node == node:
                        cycle_start_node = -1
                    return True
            return False

        found_cycle(edges[0][0], -1)        
        print(cycle_nodes)
        for u, v in reversed(edges):
            if u in cycle_nodes and v in cycle_nodes:
                return [u, v]


    def findRedundantConnection2(self, edges: List[List[int]]) -> List[int]:
        subNodes = defaultdict(list)
        for n1, n2 in edges:
            subNodes[n1].append(n2)
            subNodes[n2].append(n1)
        
        no_cycle_nodes = set() # no need. We will not revisit any node unless there is a cycle which will be caught by if node in curr_path:
        curr_path = set()
        def found_cycle(node, parent):
            if node in curr_path:
                return True
            # if node in no_cycle_nodes: 
            #     return False
            
            curr_path.add(node)

            for neighbor in subNodes[node]:
                if neighbor == parent:
                    continue
                if found_cycle(neighbor, node):
                    return True

            curr_path.remove(node)
            # no_cycle_nodes.add(node)
            return False

        found_cycle(edges[0][0], -1)        
        for u, v in reversed(edges):
            if u in curr_path and v in curr_path:
                return [u, v]