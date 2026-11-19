class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        visited = set()
        h = [[grid[0][0], 0, 0]]
        while len(h) > 0:
            time, r, c = heapq.heappop(h)
            if r == n-1 and c == n-1:
                return time
            if (r, c) in visited:
                continue
            visited.add((r,c))

            for dr, dc in dirs:
                nr, nc = dr+r, dc+c
                if not (0 <= nr <= n-1 and 0 <= nc <= n-1):
                    continue
                newTime = grid[nr][nc]
                heapq.heappush(h, [max(time, newTime), nr, nc])
        
        return -1 # this should not happen
                


        




        
        




