class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        '''
        idx: [1 2 3]
        (i) % n
        n = 3
        0 1 2 3 4 5 6
        0 1 2 0 1 2 0

        BF: loop though for each idx and run another loop to sum every subarray from i to i. If next i is i, break before any
        '''
        n = len(nums)
        maxSum = -float("inf")
        for i in range(n):
            currSum = 0
            for j in range(i, i+n):
                currSum += nums[j % n]
                maxSum = max(maxSum, currSum)
        
        return maxSum





