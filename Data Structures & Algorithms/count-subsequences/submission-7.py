class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        '''
        3:22
        base: if len(s) < len(t) return 0

        output = 1
        s=caaat, 
        i ^    
        t=cat
        j  ^

        dp[i][j] = the number of ways for s[i:] and t[j:]?
        when t[j] = "", no more char to match, all chars behind matched we are at the end, return 1?
        when s[i]="", no more char at the bank, we are run out of chars to match, return 0
        dp[i][j] = if s[i] == s[j] move i and j by 1 else I thnk we need to move i because we cant skip j. so else is dfs(i+1, j)
        '''
        if len(t) > len(s):
            return 0
        dp = {}
        def dfs(i, j):
            if j == len(t): return 1
            if i == len(s): return 0
            # if t[j:] == "": return 1
            # if s[i:] == "": return 0
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            if s[i] == t[j]:
                dp[(i,j)] = dfs(i+1, j) + dfs(i+1, j+1)
            else:
                dp[(i,j)] = dfs(i+1, j)

            return dp[(i,j)]

        return dfs(0, 0)