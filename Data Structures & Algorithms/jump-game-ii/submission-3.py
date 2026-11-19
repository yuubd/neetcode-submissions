class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        jumps = 0
        range_end = 0
        farthest = 0
        for i, n  in enumerate(nums):
            if i + nums[i] >= len(nums)-1: # we can arrive with next jump
                return jumps+1
            
            farthest = max(farthest, nums[i]+i) # the farthest we can get from pos i

            if range_end == i: # we have scanned all pos before a real jump. No other optioin. Make a jump now
                jumps += 1
                range_end = farthest # now sets new range_end for next move cuz we made a jump
            



        