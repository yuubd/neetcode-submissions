class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        7:53 stopped at 8:34

        s = ""
        p = "" or "*"
        True

        s = ""
        p = "a" or "."
        False

        s = "a"
        p = "." go to next

        dp[i][j] = whether s[i:] and p[j:] are matching
        dp[i][j] = (s[i] == p[j] or p=='.' and dfs(i+1, j+1)) or << meaning the chars at i and k match exactly need to more i and j one >>
                   (p=='*' and dfs(i+1,j+1) or dfs(i+1, j)) << meaning it s a match but we need to try either moving two together or only i cuz we could use * more
                   otherwise, False
        if i == len(s) and j == len(p) or the rest is/are * True
        if j == len(p) False
        
        dfs(0,0)
        '''


        dp = {}
        def dfs(i,j):
            if j == len(p):
                return i == len(s)
            if (i, j) in dp:
                return dp[(i, j)]
            
            matched = False
            if j+1 < len(p) and p[j+1] == "*": # next is star
                # check for char mathcing 
                useStar = False
                if i < len(s) and (s[i] == p[j] or p[j] == "."):
                    useStar = dfs(i+1, j) # use * and maybe more
                skipStar = dfs(i, j+2) # try skip star always
                matched = skipStar or useStar
            else:
                # next is not star and the chars are same, i+1 j+1
                if i < len(s) and s[i] == p[j] or p[j] == ".":
                    matched = dfs(i+1, j+1)

            dp[(i, j)] = matched
            return dp[(i, j)]


        return dfs(0, 0)


















