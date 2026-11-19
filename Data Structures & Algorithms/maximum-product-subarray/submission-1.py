class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largests_dp = [0] * len(nums)
        smallests_dp = [0] * len(nums)
        largests_dp[0] = nums[0]
        smallests_dp[0] = nums[0]

        res = largests_dp[0]
        for i, n in enumerate(nums[1:], start=1):
            largests_dp[i] = max(
                nums[i],
                largests_dp[i-1] * nums[i],
                smallests_dp[i-1] * nums[i]
            )
            smallests_dp[i] = min(
                nums[i],
                largests_dp[i-1] * nums[i],
                smallests_dp[i-1] * nums[i]
            )
            res = max(res, largests_dp[i])

        return res
