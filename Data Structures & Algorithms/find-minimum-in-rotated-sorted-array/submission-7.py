class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        get mid

        there are two cases
        min is on the left 
            then mid < nums[last] < nums[0]
        min is on the right
            then nums[last] < nums[0] < mid
        edge cases:
            1. if nums[0] < nums[last] return nums[0]
            2. 



        if nums[0] < mid: go to left
        if rightmid < mid: go to right
        until l <= r
        return the min


        '''
        l = 0
        r = len(nums)-1
        min_n = nums[0]
        while l <= r:
            mid = (l+r)//2
            min_n = min(min_n, nums[mid])
            # print("left", nums[l], "mid", nums[mid], "right", nums[r])
            if nums[r] <= nums[mid] : 
                l = mid+1
            else:
                r = mid-1

        return min_n


