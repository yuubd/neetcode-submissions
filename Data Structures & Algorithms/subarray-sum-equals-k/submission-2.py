class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixCounts = {0:1}
        total = 0
        currSum = 0
        for n in nums: 
            currSum += n
            diff = currSum - k
            if diff in prefixCounts:
                total += prefixCounts[diff]
            prefixCounts[currSum] = prefixCounts.get(currSum, 0) + 1
        return total
