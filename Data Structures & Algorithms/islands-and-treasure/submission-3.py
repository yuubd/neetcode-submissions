class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS = len(grid)
        COLS = len(grid[0])
        
        visited = set() # tuple
        pos = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    pos.append([r,c])
        
        while len(pos) > 0:
            for _ in range(len(pos)):
                r, c = pos.popleft()
                dis = grid[r][c]
                if 0 <= r-1 and grid[r-1][c] == INF:
                    grid[r-1][c] = dis + 1
                    pos.append([r-1, c])
                if r+1 <= ROWS-1 and grid[r+1][c] == INF:
                    grid[r+1][c] = dis + 1
                    pos.append([r+1, c])
                if 0 <= c-1 and grid[r][c-1] == INF:
                    grid[r][c-1] = dis + 1
                    pos.append([r, c-1])
                if c+1 <= COLS-1 and grid[r][c+1] == INF:
                    grid[r][c+1] = dis + 1
                    pos.append([r, c+1])
        return
    
    def islandsAndTreasure2(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        visited = set() # tuple
        pos = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    pos.append([r,c])
        
        dis = 0
        while len(pos) > 0:
            currPoss = len(pos)
            for _ in range(currPoss):
                r, c = pos.popleft()
                # replace th grid with dis
                if (r, c) in visited or grid[r][c] == -1:
                    continue
                grid[r][c] = dis
                visited.add((r,c))
                # add valid pos for next dis
                if 0 <= r-1:      pos.append([r-1, c])
                if r+1 <= ROWS-1: pos.append([r+1, c])
                if 0 <= c-1:      pos.append([r, c-1])
                if c+1 <= COLS-1: pos.append([r, c+1])
            dis += 1

        return