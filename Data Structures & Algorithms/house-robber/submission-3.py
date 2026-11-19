class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0, nums[0]]

        for n in range(2, len(nums)+1):

            dp.append(max(dp[n-1], dp[n-2]+nums[n-1]))
        
        return dp[len(nums)]



    def robMemo(self, nums: List[int]) -> int:
        memo = [-1] * (len(nums) + 1)

        def dp(n):
            if n == 0:
                return 0
            if n == 1:
                return nums[0]

            if memo[n] == -1:
                memo[n] = max(dp(n-1), dp(n-2)+nums[n-1])
            return memo[n]

        return dp(len(nums))