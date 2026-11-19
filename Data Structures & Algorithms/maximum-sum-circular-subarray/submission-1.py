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
            currIdx = i
            
            count = 0
            while count < n:
                currSum += nums[currIdx]
                maxSum = max(maxSum, currSum)
                currIdx = (currIdx+1) % n
                count += 1
        
        return maxSum





