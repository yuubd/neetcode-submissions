class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        '''
        idx: [1 -2 3]
        (i) % n
        n = 3
        0 1 2 3 4 5 6
        0 1 2 0 1 2 0

        BF: loop through for each idx and run another loop to sum every subarray from i to i. If next i is i, break before any

        Op: prefix and suffix max
        [.  1  -2  3] 4
        [0, 1, -1, 2]
        [3, 3,  3, 0]
        '''
        n = len(nums)
        suffixMax = [0] * (n+1)
        suffixSum = 0
        for i in range(n-1, -1, -1):
            suffixSum += nums[i]
            suffixMax[i-1] = max(suffixMax[i], suffixSum)
        print(suffixMax)

        maxSum = -float("inf")
        currMax = -float("inf")
        prefixSum = 0

        for i in range(n):
            currMax = max(0, currMax) # from k1 to k2
            currMax += nums[i]
            maxSum = max(maxSum, currMax) 
            
            prefixSum += nums[i] # from 0 tox i
            maxSum = max(maxSum, prefixSum + suffixMax[i])
            
        
        return maxSum


