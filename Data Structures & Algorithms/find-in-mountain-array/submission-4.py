class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        '''
        3:20
        This is to find the index of the target in the MountainArr.
        We need to find the peak first, and check the left and right.

        brute force is to scan, but we are limited on how many get calls we can make

        Need to use BS.
        1. Find peak
        2. run BS on left and right

        To find the peak, get the mid, look at adjacent number to see the gradient.
        if + peak is on the right, else left. If arr[mid-1] < arr[mid] > add[mid+1] then it s the peak

        states:
            l, r
        while not (arr mid-1 < arr mid < arr mid+1):
            if arr mid == target, return mid
            if arr mid-1 < arr mid < arr mid+1:
                l = mid + 1
            if arr mid-1 > arr mid > arr mid+1:
                r = mid - 1
        Run BS on 0 to mid and mid+1 to mid the target.
        '''
        
        length = mountainArr.length()
        l, r = 0, length-1
        mid = 0
        midNum = 0
        while True:
            mid = (l+r) // 2
            prevMidNum = mountainArr.get(mid-1) if mid > 0 else -1
            midNum = mountainArr.get(mid)
            nextMidNum = mountainArr.get(mid+1) if mid < length else 10001
            if prevMidNum < midNum > nextMidNum:
                break
            
            if prevMidNum < midNum < nextMidNum:
                l = mid + 1
            
            elif prevMidNum > midNum > nextMidNum:
                r = mid -1 
            
        print(mid)
        storedMid = mid

        l, r = 0, storedMid
        # BS on left
        while l <= r:
            mid = (l+r) // 2
            midVal = mountainArr.get(mid)
            if midVal == target:
                return mid
            if midVal < target:
                l = mid+1
            else:
                r = mid-1

        l, r = storedMid, length-1
        # BS on right
        print(l, r)
        while l <= r:
            mid = (l+r) // 2
            midVal = mountainArr.get(mid)
            if midVal == target:
                return mid
            if target > midVal:
                r = mid-1
            else:
                l = mid+1

        return -1






















