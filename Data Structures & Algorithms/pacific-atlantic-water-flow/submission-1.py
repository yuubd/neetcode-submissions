class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
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
