class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        '''
        1:25
        so from the example, the start and the end have to be visited to produce the res, eh?
        The the hard base case will be if start or end is not 0, return -1.
        And the res is path of 0s, eh?

        This is BFS to find the shortesst in 8 way/

        State:
            visited no need
            dequeue of next position and the path. If any route leads to the dest, return,
            otherwise return -1 after the loop
        '''
        

        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        q = deque([(0, 0, 1)])
        dirs = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,1), (-1,-1), (1,-1)]

        while q:
            r, c, path = q.popleft()

            if grid[r][c] == 1: # 
                continue 
            grid[r][c] = 1

            if r == n-1 and c == n-1: # ans
                return path

            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if not (0 <= nr <= n-1 and 0 <= nc <= n-1):
                    continue
                if grid[nr][nc] == 1: # dont go to 1s
                    continue

                q.append((nr, nc, path+1))

        return -1









