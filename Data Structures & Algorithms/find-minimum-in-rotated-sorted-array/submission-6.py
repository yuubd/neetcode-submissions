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
            mid_n = nums[mid]
            min_n = min(min_n, mid_n)
            # print("left", nums[l], "mid", nums[mid], "right", nums[r])
            if nums[l] <= nums[mid] <= nums[r]: 
                return min(nums[l], min_n)
            if nums[mid] <= nums[r] <= nums[l]:
                r = mid-1
            if nums[r] <= nums[l] <= nums[mid]:
                l = mid+1

        return min_n 


