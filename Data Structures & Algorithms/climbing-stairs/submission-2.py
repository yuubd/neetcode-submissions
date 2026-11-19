class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dp(steps):
            if steps == 1:
                memo[1] = 1
            if steps == 2: 
                memo[2] = 2

            if steps not in memo:
                memo[steps] = dp(steps-1) + dp(steps-2)
            return memo[steps]
        
        return dp(n)