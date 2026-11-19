class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0] * m for _ in n]
        memo[m-1][n-1] = 1

        for r in range(m-1, -1, -1):
            for c in range(c-1, -1, -1):
                if r == m-1 and c == n-1: continue
                memo[r][c] = memo[r+1][c] + memo[r][c+1]
        return memo[0][0]



    def uniquePaths(self, m: int, n: int) -> int:
        '''
        if currR and currC = m-1, n-1 then res += 1
        So there is only two options r+1 c+1

        We can use dfs
        '''
        memo = {}
        def dfs(r, c):
            if r == m or c == n:
                return 0
            if r == m-1 and c == n-1:
                return 1
            
            if (r, c) in memo:
                return memo[(r, c)]

            memo[(r, c)] = dfs(r, c+1) + dfs(r+1, c)
            return memo[(r, c)] 
        
        return dfs(0, 0)

