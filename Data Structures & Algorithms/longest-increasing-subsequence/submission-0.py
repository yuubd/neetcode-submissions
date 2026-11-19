class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        res = 1

        for i, n_i in enumerate(nums):
            for j, n_j in enumerate(nums[:i]):
                if n_j < n_i:
                    dp[i] = max(dp[i], 1 + dp[j])
                    res = max(dp[i], res)
        return res