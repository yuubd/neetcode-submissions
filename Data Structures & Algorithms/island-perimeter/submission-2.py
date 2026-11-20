class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        RS, CS = len(grid), len(grid[0])        

        q = deque([
            next(
                (r,c) 
                for r in range(RS) 
                for c in range(CS) 
                if grid[r][c] == 1)
        ])
        visited = set()
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        perimeter = 0
        while q:
            r, c = q.popleft()
            if (r, c) in visited:
                continue
            visited.add((r,c))
            perimeter += 4

            for dr, dc in dirs:
                nr, nc = dr+r, dc+c
                if not (0 <= nr <= RS-1 and 0 <= nc <= CS-1):
                    continue
                if grid[nr][nc] == 0:
                    continue
                perimeter -= 1
                q.append((nr, nc))
        
        return perimeter



        