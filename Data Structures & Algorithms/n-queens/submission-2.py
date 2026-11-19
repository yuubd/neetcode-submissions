class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
        It s finding the permutation of positions that works
        so choose  0       6 choices for col 0 * 4 so it s 4*3*2*1 n!
                1  2  3
              2 3 1 3 1 2
              3 2 3 1 2 1

        There must be one queen at each row and col.

        Do the same permutation with diag checks

        if row > n
        for each row, 0 to n,
            if curr r,c in the cant use set for col row and diags, continue
            if not, add the pos to res
            mark the set
            dfs to next row << will return if found answer
            if not returned, remove all added above
        '''
        posLists = []
        colSet = set()
        diagSet = set() # for both diag r-c and anti diag r+c
        revDiagSet = set()
        def backtrack(r, queenPos):
            if r == n:
                posLists.append(list(queenPos).copy())
                return
            for c in range(n):
                if c in colSet or c-r in diagSet or c+r in revDiagSet:
                    continue
                colSet.add(c)
                diagSet.add(c-r)
                revDiagSet.add(c+r)

                queenPos.add((r,c))
                backtrack(r+1, queenPos)

                queenPos.remove((r,c))
                colSet.remove(c)
                diagSet.remove(c-r)
                revDiagSet.remove(c+r)
        
        backtrack(0, set())

        res = []
        for posList in posLists:
            board = [["."] * n for _ in range(n)]
            for r, c in posList:
                board[r][c] = "Q"
            res.append(["".join(r) for r in board])
        
        return res

        

                

        
            