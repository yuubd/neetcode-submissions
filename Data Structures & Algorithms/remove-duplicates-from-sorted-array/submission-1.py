class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        l, r
        r moves and if r == r-1 keep moving the r until not,
        l = r
        '''

        l = r = 0
        while r < len(nums):
            nums[l] = nums[r]
            while r < len(nums) and nums[r] == nums[l]:
                r += 1
            l += 1
        return l
            
            

        if len(nums) == 1: return 1

        i = 0
        for n in nums[1:]:
            if nums[i] == n:
                continue
            i += 1
            nums[i] = n
        
        return i + 1
