class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        nToNodes = defaultdict(list)
        for i in range(n):
            nToNodes[i] = []
        for n1, n2 in edges:
            nToNodes[n1].append(n2)
            nToNodes[n2].append(n1)
        
        def dfs(n, parent):
            if n in visited:
                return
            visited.add(n)

            for next_node in nToNodes[n]:
                if next_node == parent:
                    continue
                dfs(next_node, n)
        res = 0
        for node in range(n):
            if node in visited:
                continue
            if nToNodes[node] == []:
                res += 1
                visited.add(node)
                continue
            dfs(node, -1)
            res +=1

        return res

        