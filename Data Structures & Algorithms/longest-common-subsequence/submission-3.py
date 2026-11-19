class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
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

    def longestCommonSubsequenceBFS(self, text1: str, text2: str) -> int:
        '''
        bottom up
        '''
        dp = [[0] * len(text1) for _ in range(len(text2))]
        dp

        return dfs(0, 0)