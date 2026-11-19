class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        visited = set() # tuple
        pos = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    pos.append([r,c])
                    # visited.add((r,c))
        # print(pos)
        # print(visited)

        
        dis = 0
        while len(pos) > 0:
            currPoss = len(pos)
            # print("dis", dis)
            for _ in range(currPoss):
                r, c = pos.popleft()
                # replace th grid with dis
                if (r, c) in visited or grid[r][c] == -1:
                    continue
                grid[r][c] = dis
                # print([r,c])
                visited.add((r,c))
                # add valid pos for next dis
                if 0 <= r-1:      pos.append([r-1, c])
                if r+1 <= ROWS-1: pos.append([r+1, c])
                if 0 <= c-1:      pos.append([r, c-1])
                if c+1 <= COLS-1: pos.append([r, c+1])
            dis += 1
        # print(grid)
            


        
        return