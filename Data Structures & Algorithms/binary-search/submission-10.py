class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Binary search
        get the mid idx
        match target
        if not see if the nums[idx] greater or smaller
        if smaller the index moves left, otherwise right
        until find, if not retuen -1 
        [-1,0,2,4,6,8]
        05 5/2 2
        35 8/2 4
        33 6/2 3
        32 exit
        '''
        l_idx = 0
        r_idx = len(nums)-1
        while l_idx <= r_idx :
            mid_idx = int((l_idx + r_idx) / 2)
            if nums[mid_idx] == target:
                return mid_idx
            if target < nums[mid_idx]:
                r_idx = mid_idx-1
            else:
                l_idx = mid_idx+1
            

        return -1