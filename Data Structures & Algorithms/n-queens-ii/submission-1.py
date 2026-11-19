class Solution:
    def totalNQueens(self, n: int) -> int:
        '''
        8:50
        There will be one queen per rows and columns.
        There are n-1 many diagonals

        We need to try each cell in a row while checking the diagonals.
        Backtracking.
        When the nth queend is placed, increment the res.


        n = 1
        for r in rows
            for c in cols
                the cell is allowed, add the pos to queens and col the diag and anti diag
                if queens len if m then return
        It has to be dfs to backtrack 

        so params: row, col
            if row is n, meaning we have successfully visited all rows, return 1
            check the col, and diags visited set.
            try with the next col and then skip col.
        return the max
        
        Time: O(2^n) for try or not try tree
        space: O(n) for keeping the visited sets
        '''

        visitedCols = set()
        visitedDiag = set()
        visitedAntiDiag = set()
        
        res = 0
        def dfs(r):
            nonlocal res
            if r == n:
                res += 1
            
            for c in range(n):
                if c in visitedCols or c-r in visitedDiag or c+r in visitedAntiDiag:
                    continue

                visitedCols.add(c)
                visitedDiag.add(c-r)
                visitedAntiDiag.add(c+r)
                dfs(r+1)
                
                visitedCols.remove(c)
                visitedDiag.remove(c-r)
                visitedAntiDiag.remove(c+r)
            
        dfs(0)

        return res
            













