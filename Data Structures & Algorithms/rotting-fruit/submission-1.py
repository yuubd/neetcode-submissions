class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = [[False] * COLS for _ in range(ROWS)]
        
        fresh = 0
        rotten = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    rotten.append([r, c])
                    visited[r][c] = 0
        print(fresh)
        print(rotten)
        directions = [[1,0],[-1,0],[0,1],[0,-1]] # 4 ways
        max_time = 0 # might not need
        while len(rotten) > 0:
            for _ in range(len(rotten)):
                r, c = rotten.popleft()
                for dr, dc in directions:
                    newR, newC = r+dr, c+dc
                    # boundary and 1 check and visited check
                    if not (0 <= newR <= ROWS-1 and 0 <= newC <= COLS-1): continue
                    if grid[newR][newC] != 1: continue
                    if visited[newR][newC] != False: continue
                    fresh -= 1
                    visited[newR][newC] = visited[r][c] + 1
                    rotten.append([newR, newC])
                    max_time = max(max_time, visited[newR][newC])        
        return max_time if fresh == 0 else -1


        