class Solution:
    def longestCommonSubsequenceDFS(self, text1: str, text2: str) -> int:
        '''
        top down
        '''
        dp = [[-1] * len(text1) for _ in range(len(text2))]
        def dfs(i, j):
            # covers all base cases no need to add col and row
            if i == len(text2) or j == len(text1): 
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if text2[i] == text1[j]:
                dp[i][j] = 1 + dfs(i+1, j+1)
            else:
                dp[i][j] = max(dfs(i+1, j), dfs(i, j+1))

            return dp[i][j]

        return dfs(0, 0)

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        bottom up
        '''
        dp = [[0] * (len(text1)+1) for _ in range(len(text2)+1)]
        for r in range(len(text2), -1, -1):
            for c in range(len(text1), -1, -1):
                if r == len(text2) or c == len(text1):
                    continue
                if text1[c] == text2[r]:
                    dp[r][c] = 1 + dp[r+1][c+1]
                else:
                    dp[r][c] = max(dp[r+1][c], dp[r][c+1])
        return dp[0][0]