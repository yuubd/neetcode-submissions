class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjMap = defaultdict(list)
        for u, v, w in times:
            adjMap[u].append([v, w])

        h = [[0, k]] # heap is [time it needs, nextNode]
        visited = set()
        res = -1
        while len(h) > 0:
            t, node = heapq.heappop(h)
            if node in visited:
                continue
            visited.add(node)
            res = max(res, t)
            neighbors = adjMap[node]
            for v, w in neighbors:
                heapq.heappush(h, [t+w, v])
        
        return res if len(visited) == n else -1
