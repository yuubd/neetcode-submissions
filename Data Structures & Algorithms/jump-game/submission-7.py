class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, nums[i]+i)
        return True
    
    def canJumpBackward(self, nums: List[int]) -> bool:
        dest = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= dest:
                dest = i
        return dest <= 0