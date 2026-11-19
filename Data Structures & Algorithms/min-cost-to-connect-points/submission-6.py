class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        '''
        Prim's = minimum spanning tree cuz it is to connect all nodes with min distance
        Could start from any. For this one, start from points[0]
        1. 0 will join the group(heap) for free push in heap [cost, dest]
        2. while visited len < len(points)
             curr cost and dest = heap pop # this means we are adding the dest to the group
             if dest in visited: continue
             add in visited
             add the cost to the res
             for all points except for curr dest:
               get the dist(cost) and add to heap [curr cost + dist, new dest]
        '''
        def getDist(frm, to):
            return abs(points[frm][0] - points[to][0]) + abs(points[frm][1] - points[to][1])

        n = len(points)
        h = [[0, 0]] # cost, idx
        visited = set()
        res = 0
        while len(visited) < n:
            cost, currPntIdx = heapq.heappop(h)
            if currPntIdx in visited:
                continue
            visited.add(currPntIdx)
            res += cost
            for destPntIdx in range(n): # range(currPntIdx, n)
                # from the next of currPoint to the end
                if destPntIdx not in visited:
                    costToDest = getDist(currPntIdx, destPntIdx)
                    heapq.heappush(h, [costToDest, destPntIdx])
        
        return res
