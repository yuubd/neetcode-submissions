class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for l in range(n-1, -1, -1): # from bottome to 0 row 
            for r in range(l, n): # from bottome to 0 row 
                # diagonal
                if l == r: dp[l][r] = True
                
                # The outer chars are the same
                if s[l] == s[r]:
                    substr = s[l:r+1]
                    # when length is <= 2, no need to check the inner
                    if len(substr) <= 2:
                        dp[l][r] = True
                        res = substr if len(substr) > len(res) else res
                        

                    # Check inner only
                    elif dp[l+1][r-1]:
                        dp[l][r] = True
                        # update max
                        res = substr if len(substr) > len(res) else res
                    # else is False
                # else is False
        return res

        