class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        return max(self.maxCost(len(nums)-1, nums[1:]), self.maxCost(len(nums)-1, nums[:-1]))

            
    def maxCost(self, n, costs):
        memo = [-1] * (len(costs)+1)
        
        def dp(n):
            if n == 0: return 0
            if n == 1: return costs[0]
            if memo[n] == -1:
                memo[n] = max(dp(n-1), dp(n-2)+costs[n-1])
            return memo[n]

        return dp(len(costs))