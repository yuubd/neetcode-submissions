class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific = [[False] * COLS for _ in range(ROWS)]
        atlantic = [[False] * COLS for _ in range(ROWS)]
        res = []

        dirs = [(-1,0), (1,0), (0,-1), (0,1)]

        pacific_q = deque()
        atlantic_q = deque()
        
        def bfs(q, ocean):
            while len(q) > 0:
                r, c = q.popleft()
                print(r, c)
                if ocean[r][c] == True:
                    continue
                ocean[r][c] = True
                for dr, dc in dirs:
                    nr, nc = dr+r, dc+c
                    if 0 <= nr <= ROWS-1 and 0 <= nc <= COLS-1:
                        if heights[nr][nc] >= heights[r][c]: 
                            q.append([nr, nc])

        # add all pacific border cells
        for c in range(COLS): # top
            pacific_q.append([0, c])
        for r in range(ROWS): # left
            pacific_q.append([r, 0])

        # add all atlantic border cells
        for c in range(COLS): # bottom
            atlantic_q.append([ROWS-1, c])
        for r in range(ROWS): # right
            atlantic_q.append([r, COLS-1])
        
        bfs(pacific_q, pacific)
        bfs(atlantic_q, atlantic)

        # find the intersactions and append in res
        for r in range(ROWS):
            for c in range(COLS):
                if pacific[r][c] and atlantic[r][c]:
                    res.append([r, c])
        return res        
    
    
    def pacificAtlanticDFS(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        res = []

        dirs = [(-1,0), (1,0), (0,-1), (0,1)]

        def dfs(r, c, visited):
            if (r, c) in visited:
                return # visited, no need to explore more
            visited.add((r, c))

            # explore other directions
            for dr, dc in dirs:
                nr, nc = dr+r, dc+c
                if 0 <= nr <= ROWS-1 and 0 <= nc <= COLS-1:
                    # it s backward, so r < nr
                    if heights[nr][nc] >= heights[r][c]: 
                        dfs(nr, nc, visited)
            return 
        
        # visit all cells that are reachable from pacific borders
        for c in range(COLS): # top
            # this means 0, c are the borders(reachable), we need to add them
            dfs(0, c, pacific)
        for r in range(ROWS): # left
            dfs(r, 0, pacific)

        # visit all cells that are reachable from atlantic borders
        for c in range(COLS): # bottom
            dfs(ROWS-1, c, atlantic)
        for r in range(ROWS): # right
            dfs(r, COLS-1, atlantic)

        # find the intersactions and append in res
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res
