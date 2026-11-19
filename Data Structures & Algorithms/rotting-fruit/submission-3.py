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

        directions = [[1,0],[-1,0],[0,1],[0,-1]] # 4 ways
        time = 0 # might not need
        while len(rotten) > 0 and fresh > 0:
            for _ in range(len(rotten)):
                r, c = rotten.popleft()
                for dr, dc in directions:
                    newR, newC = r+dr, c+dc
                    # boundary and 1 check and visited check
                    if not (0 <= newR <= ROWS-1 and 0 <= newC <= COLS-1): continue
                    if grid[newR][newC] != 1: continue
                    grid[newR][newC] = 2
                    rotten.append([newR, newC])
                    fresh -= 1
            time += 1
  
        return time if fresh == 0 else -1


        