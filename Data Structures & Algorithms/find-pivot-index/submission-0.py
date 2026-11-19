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

        prefixSums = [0] * (len(nums)+1)
        postfixSums = [0] * (len(nums)+1)

        summ = 0
        for i, n in enumerate(nums):
            summ += n
            prefixSums[i+1] = summ
        summ = 0
        for i, n in enumerate(reversed(nums)):
            summ += n
            postfixSums[i+1] = summ

        postfixSums.reverse()
        print(prefixSums)
        print(postfixSums)

        for i in range(len(nums)):
            leftSum = prefixSums[i] if i else 0
            rightSum = postfixSums[i+1]
            

            if leftSum == rightSum:
                return i
        return -1
    