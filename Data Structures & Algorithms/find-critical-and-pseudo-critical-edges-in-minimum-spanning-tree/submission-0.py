class UnionFind:
    def __init__(self, n):
        self.n = n
        self.Parent = list(range(n + 1))
        self.Size = [1] * (n + 1)

    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        self.n -= 1
        if self.Size[pu] < self.Size[pv]:
            pu, pv = pv, pu
        self.Size[pu] += self.Size[pv]
        self.Parent[pv] = pu
        return True

    def isConnected(self):
        return self.n == 1

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        '''
        12:52

        base case and trivial case all edges are used for MST
            n == e-1 then return the edges
          0
        0---1
       1|   |2
        3---2
          1
        output = [01, 03, 32] []
        '''
        
        ''' Kuskal
        add all edges in the heap of (weight, frm, to)
        
        edges = []
        cost
        use unionFind = UnionFind(n)
            unionFind.union(int1, int2) # true if int1 and 2 are unioned
        append from to the edges
        increment cost += weight

        return the cost of edges
        '''
        for i, (n1, n2, w) in enumerate(edges):
            edges[i] = (w,n1,n2,i)
        edges.sort() # weight, from, to

        def findMSTCostWithInclude(includeIdx, include):
            unionFind = UnionFind(n)
            cost = 0
            
            if include:
                cost += edges[includeIdx][0]
                unionFind.union(edges[includeIdx][1], edges[includeIdx][2])

            for i, (w, n1, n2, originalIdx) in enumerate(edges):
                if i == includeIdx:
                    continue
                # false meaning they are already in the same union
                if not unionFind.union(n1, n2):
                    continue   
                cost += w
            return cost if unionFind.isConnected() else float("inf")
        
        totalCost = findMSTCostWithInclude(-1, False)
        critical, pseudo = [], []
        for i, (w, n1, n2, originalIdx) in enumerate(edges):
            # testing if ith edge is critical when exclude
            if totalCost < findMSTCostWithInclude(i, False): 
                critical.append(originalIdx)
            # testing if ith edge is pseudo or not
            elif totalCost == findMSTCostWithInclude(i, True):
                pseudo.append(originalIdx)
        
        return [critical, pseudo]

        