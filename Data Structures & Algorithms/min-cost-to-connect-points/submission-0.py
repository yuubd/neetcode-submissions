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
            return abs(frm[0] - to[0]) + abs(frm[1] - to[1])

        n = len(points)
        h = [[0, 0, (points[0][0], points[0][1])]] # cost, idx, (r, c)
        visited = set()
        res = 0
        while len(visited) < n:
            cost, i, currPoint = heapq.heappop(h)
            if currPoint in visited:
                continue
            visited.add(currPoint)
            res += cost
            for j, destPoint in enumerate(points, start = i + 1):
                costToDest = getDist(currPoint, destPoint)
                # from the next of currPoint to the end
                heapq.heappush(h, [costToDest, j, (destPoint[0], destPoint[1])])
        
        return res
