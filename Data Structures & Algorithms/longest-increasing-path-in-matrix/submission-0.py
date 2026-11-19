class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # -math.Inf
        ROWS, COLS = len(matrix), len(matrix[0])
        longest = 0
        
        dp = {}
        def dfs(r, c, prev):
            if not (0 <= r <= ROWS-1 and 0 <= c <= COLS-1):
                return 0
            if matrix[r][c] <= prev:
                return 0
            if (r, c) in dp: 
                return dp[(r,c)]
            
            curr = matrix[r][c]
            dp[(r, c)] = 1 + max(
                dfs(r+1, c, curr),
                dfs(r-1, c, curr),
                dfs(r, c+1, curr),
                dfs(r, c-1, curr)
            )

            return dp[(r, c)]

        for r in range(ROWS):
            for c in range(COLS):
                longest = max(longest, dfs(r, c, -math.inf))
        return longest