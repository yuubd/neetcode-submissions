class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = -float("inf")
        for n in nums:
            currSum += n
            maxSum = max(maxSum, currSum)
            currSum = max(currSum, 0)

        return maxSum