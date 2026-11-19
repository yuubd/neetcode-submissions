class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1 # one way to choose ""
        dp[1] = 1 if s[0] != "0" else 0
        
        # we only need dp[0] just in case the recursion hits dp[0] correct?
        for i in range(2, n+1): # cuz we want dp[3] is for the ways for the last char s[len(s)-1] which is s[2]. i is for dp index not string idx 
            curr_n= s[i-1]
            one_prev_n = s[i-2]
            if curr_n != "0": # cuz if prev n is 0, it doesnt matter cuz dp[i-1] should still have correct number of ways. We need to only look at the curr_n is 0 or not.
                dp[i] += dp[i-1]
            if one_prev_n != "0" and int(one_prev_n + curr_n) <= 26:
                dp[i] += dp[i-2]
            
            
        return dp[n]