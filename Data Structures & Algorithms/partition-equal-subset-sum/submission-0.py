class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2 
        dp = [False] * (target+1)
        dp[0] = True

        for n in nums:
            for i in range(target, n-1, -1): # n-1 is bettwe -1 works but the between is redundant 
                if 0 <= i-n and dp[i-n]:
                    dp[i] = True
        return dp[target]
