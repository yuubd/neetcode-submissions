class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        dp[i][holding] = max profit of day i onwards 
        dp[1][True] = the max profit at day prices[1:] when holding
        if i == len(prices) return 0 as no day to sell or buy
            if holding: 
                dp[i][True] =  -prices[i] + dp[i+2][False]
                skip: dp[i+1][False]
            if not holding:
                dp[i][False] = prices[i] + dp[i+1][True] 
                skip: dp[i+1][True]
        return the max profit at dp[0][True]
        '''

        dp = [[0] * 2 for _ in range(len(prices))]

        def dfs(i, holding):
            if i >= len(prices):
                return 0
            if dp[i][holding]:
                return dp[i][holding]
            
            if holding:
                dp[i][True] = max( # we are holding it now
                    prices[i] + dfs(i+2, False), # sell + and tmr is cool afer sell and the next day we will be not holding
                    dfs(i+1, True) # we done sell go to tmr 
                )
            else:
                dp[i][False] = max( # we are not holding today
                    -prices[i] + dfs(i+1, True), # buy today and tmr we will be holding
                    dfs(i+1, False) # we dont do any go to next day
                )

            return dp[i][holding]
        
        return dfs(0, False)
