class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(i, r):
            if r == amount:
                return 1
            if i == len(coins):
                return 0
            if (i, r) in dp:
                return dp[(i, r)]

            k = 0
            total = 0
            while r + k * coins[i] <= amount:
                total += dfs(i+1, r+k*coins[i])
                k += 1
            dp[(i, r)] = total
            return dp[(i, r)]

        return dfs(0, 0)