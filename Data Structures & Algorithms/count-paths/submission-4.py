class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        if currR and currC = m-1, n-1 then res += 1
        So there is only two options r+1 c+1

        We can use dfs
        '''
        ROWS, COLS = m, n
        memo = {}

        def dfs(r, c):
            if r == m or c == n:
                return 0
            if r == m-1 and c == n-1:
                return 1

            down = memo[(r, c+1)] if (r, c+1) in memo else dfs(r, c+1)
            right = memo[(r+1, c)] if (r+1, c) in memo else dfs(r+1, c)
            memo[(r, c)] = down + right
            return memo[(r, c)]
        
        return dfs(0, 0)

