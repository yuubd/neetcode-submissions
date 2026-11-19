

class Solution:
    def getDist(self, frm, to):
            return abs(frm[0] - to[0]) + abs(frm[1] - to[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        '''
        Brute force: try all dfs with backtracking and return the min cost
        time: O(n^n)
        space: O(n^2 + n) making the distace matrix and recursion callstack

        Kruskal:
        Get distances of each distance and add to heap ordered by the cost, from, to
        mts = [] 
        cost = 0
        while mts len is < len(points):
            pop from the heap << the cheapest next.
            add to to mts. ad from only for the first time
        return cost
        '''
        n = len(points)
        
        parent = list(range(n)) # 0 1 2 .. n-1 saying their parents are themselves
        # it s to update x's captain to its parent's captain
        def findCaptain(x): # 2 2 2
            while parent[x] != x: # 1 != 0
                parent[x] = parent[parent[x]] # parent[0] = parent[1] = 2
                x = parent[x] # x = 2
            return x
            
        
        h = [] # heap of cost, from, to
        for i in range(n):
            for j in range(i+1, n):
                frm = points[i]
                to = points[j]
                if frm != to:
                    heapq.heappush(h, (self.getDist(frm, to), i, j))
        # print(h)
        
        cost = 0
        while len(h) > 0:
            cheapest, frm, to = heapq.heappop(h)

            frmCaptain, toCaptain = findCaptain(frm), findCaptain(to)
            if frmCaptain == toCaptain:
                continue
            parent[toCaptain] = frmCaptain
            cost += cheapest

        return cost

        

    def minCostConnectPointsPrim(self, points: List[List[int]]) -> int:
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
            for destPntIdx in range(n): # range(currPntIdx, n) << not cuz order is not kept
                # from the next of currPoint to the end
                if destPntIdx not in visited:
                    costToDest = getDist(currPntIdx, destPntIdx)
                    heapq.heappush(h, [costToDest, destPntIdx])
        
        return res
