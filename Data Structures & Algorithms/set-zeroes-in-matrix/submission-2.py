class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        '''
        1. loop matrix once and store the positions of 0s << brute force
        2. have sets for rows and colums to indicate which rows and cols are 
            loop, add col and row in the sets.
            run on the sets and replace the rows and cols to 0s
        states
        rowSet, colSet
        '''

        ROWS, COLS = len(matrix), len(matrix[0])
        rowSet, colSet = set(), set()

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    rowSet.add(r)
                    colSet.add(c)
        # print(rowSet)
        # print(colSet)
        tmp = [0] * COLS
        for r in rowSet:
            matrix[r] = tmp
        # print(matrix)

        for c in colSet:
            for r in range(ROWS):
                matrix[r][c] = 0






        
        