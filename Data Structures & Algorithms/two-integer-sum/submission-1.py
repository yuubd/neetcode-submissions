class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        set the array
        for each n i nums find the target - n
        '''
        d = {n: i for i,n in enumerate(nums)}
        
        for i, n in enumerate(nums):
            if target-n in d and d[target-n] != i:
                return [i, d[target-n]]

        return []