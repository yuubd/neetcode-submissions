class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0, 0]

        for n in range(2, len(cost)+1):
            if n == len(dp):
                dp.append(min(dp[n-1]+cost[n-1], dp[n-2]+cost[n-2]))
        
        return dp[n]
            
            











def minCostClimbingStairsMemo(self, cost: List[int]) -> int:
        memo = [0] * (len(cost)+1)

        def dp(n):
            if n <= 1: 
                return memo[n]

            if memo[n] == 0:
                memo[n] = min(dp(n-1)+cost[n-1], dp(n-2)+cost[n-2])

            return memo[n]

        return dp(len(cost))
