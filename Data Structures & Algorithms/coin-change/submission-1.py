class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        
        for curr_amount in range(1, amount+1):
            for curr_coin in coins:
                remaining = curr_amount - curr_coin
                if remaining < 0:
                    continue
                # dp[current_amount] is already inf.
                dp[curr_amount] = min(dp[curr_amount], 1+dp[remaining])
        
        return dp[amount] if dp[amount] != float("inf") else -1
