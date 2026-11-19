class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        start=0
        end=len-1
        mid=(start+end)/2
        if mid = target: return mid
        if mid < target then see if target < mid+1 and mid < len
        if target < mid then see if mid-1 < target and mid > 0
        '''

        start = 0
        end = len(nums)-1
        res = len(nums)
        while start <= end:
            mid = int((start + end) / 2)
            # print("start", start, "end", end, "mid", mid)
            if target == nums[mid]: return mid
            if target < nums[mid]:
                res = mid
                end = mid-1
            else: # target < nums[mid]:
                start = mid+1
            # if count == 0 :break
            # else: count -= 1
        return res




