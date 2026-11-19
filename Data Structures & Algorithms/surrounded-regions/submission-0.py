class Solution:
    def solve(self, board: List[List[str]]) -> None:
        '''
        Is finding the Os that are not connected to any border cells.
        So we can start from border O cells, run dfs, mark visited
        In another go over, convert all unvisted Os to X
        '''
        ROWS, COLS = len(board), len(board[0])
        visited = [[0]*COLS for _ in range(ROWS)]
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r, c):
            if visited[r][c]:
                return
            visited[r][c] = True
            
            if board[r][c] == "X":
                return

            for dr, dc in dirs:
                nr, nc = dr+r, dc+c
                if 0 <= nr <= ROWS-1 and 0 <= nc <= COLS-1:
                    dfs(nr,nc) 

            return
        
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or r == ROWS-1 or c == 0 or c == COLS-1:
                    dfs(r, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if visited[r][c] == False:
                    board[r][c] = "X"
        return