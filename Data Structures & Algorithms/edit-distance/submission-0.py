class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        need a map of char to indexes..?
        S: dp[i][j] = the min number of operations to match word1[i:] to word2[j:]
        B: if i == len(word1): return len(word2)-j << no more chars in word1, insert remaining of word2
           if j == len(word2): return len(word1)-i<< no more chars in word2, delete remaining of word1
           if j == len(word2) and i == len(word1), return 0 (no more chars on both)
        L: dp[i][j] = dfs(i+1, j+1) if word1[i] == word2[j], << match no opr
                      min of 1 + dfs(i+1, j) if word1[i] != word2[j], << delete 
                             1 + dfs(i, j+1) if word1[i] != word2[j], << insert
                             1 + dfs(i+1, j+1) if word1[i] != word2[j], << insert
        A: dfs(0, 0)
        '''

        dp = {}

        def dfs(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if (i, j) in dp:
                return dp[(i,j)]
            
            if word1[i] == word2[j]:
                dp[(i,j)] = dfs(i+1, j+1)
            else:
                dp[(i,j)] = min(
                    1 + dfs(i, j+1),
                    1 + dfs(i+1, j),
                    1 + dfs(i+1, j+1),
                )
            return dp[(i,j)]
        return dfs(0,0)