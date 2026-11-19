class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        dp[i][can_buy] = max profit of day i onwards 
        if i == len(prices) return 0 as no day to sell or buy
            if can_buy: 
                dp[i][True] = dp[i+1][False] - prices[i]
                skip: dp[i+1][True]
            if cant_buy:
                dp[i][False] = dp[i+1][True] + prices[i]
                skip: dp[i+1][False]
        return the max profit at dp[0][True]
        '''
        dp = [[0] * 2 for _ in range(len(prices)+1)]
        
        def dfs(i, can_buy):
            print(i)
            if i >= len(prices):
                return 0
            if dp[i][can_buy]:
                return dp[i][can_buy]
            if can_buy:
                prev = dfs(i+1, False)
                dp[i][True] = max(prev - prices[i], dfs(i+1,True))
            else:
                prev = dfs(i+2, True)
                dp[i][False] = max(prev + prices[i], dfs(i+1,False))
            return dp[i][can_buy]

        return dfs(0, True)

        