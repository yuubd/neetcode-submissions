class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        direction: [r -> l -> d -> u]
        visitied: stores only the indexs or numbers
        return when res len == m*n or none of the directions is working
        also need i j indexs
        '''

        ROWS, COLS = len(matrix), len(matrix[0])
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        res = []
        visited = set()
        dr, dc = dirs[0]
        r = c = 0
        i = 0
        while len(res) < ROWS * COLS:
            res.append(matrix[r][c])
            visited.add((r,c))

            if not (0 <= r+dr <= ROWS-1 and 0 <= c+dc <= COLS-1) or \
                (dr+r, dc+c) in visited:
                i = (i + 1) % 4
                dr, dc = dirs[i]
            
            r, c = dr+r, dc+c
        
        return res 
