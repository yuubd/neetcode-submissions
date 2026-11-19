class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        1. Can nums len less than k? no
        

        1. from l r at 0, expand the window to k and get the max = max(nums[0:k])
        2. while incrementing l and r one by one,
            update max: here we need to keep track of the max of the window
            two options, stack or heap.
            have a stack. push if nothing in it => for next, check the top item, if smaller, push.

        keep max st
        keep max value and only add when see greater or equal value
        deque and stack

        q = 1 2 1
        h = 1,0 1,1 2,1 heap compare the first item and then second if tie
        
        2 3 1
        [2,3]

        res = [3, 3]
        
        while r <= len(nums)-1
            append nums[r] into heap 
            r += 1

            if r - l + 1 the size > k:
                if nums[l] == h[-1]:
                    h.pop()
                l += 1
            res.append(h[-1])
        return res
        

        before the size(r-l+1) is less then k, add n at r into heap
        move l and r, if we see larger value, we can replace or just push
        after the size is k, push the max to the res at the end of each loop

        '''
        h = [] # [val, idx] higher value first, lower idx first
        l = 0
        res = []

        # while r <= len(nums)-1:
        for r, n in enumerate(nums):
            heapq.heappush(h, [-nums[r], r])
            if r+1 - l < k:
                continue
            if r+1 - l > k:
                while h[0][1] <= l:
                    heapq.heappop(h) 
                l += 1

            # we have the k size window
            # print(h, r+1-l)
            res.append(-h[0][0])

        return res
            
            









        



