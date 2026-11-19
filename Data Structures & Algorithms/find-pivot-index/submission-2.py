class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        create
        prefix and postfix
        
        for each idx
            see if prfix to i-1 == post fix from i+1
            return the idx
        retuen -1
        '''
        total = sum(nums)

        leftSum = 0

        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
            
        return -1

        