class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        l, r
        r moves and if r == r-1 keep moving the r until not,
        l = r
        '''
        if len(nums) == 1: return 1

        i = 0
        for n in nums[1:]:
            if nums[i] == n:
                continue
            i += 1
            nums[i] = n
        
        return i + 1

        '''
        1 2 3 2 2 3
            i     n
  
        '''



