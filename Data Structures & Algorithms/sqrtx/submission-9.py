class Solution:
    def mySqrt(self, x: int) -> int:
        
        '''
        from 0 to x
            need to find the mid*mid < x < (mid+1)*(mid+1) and return mid
        '''

        l, r = 0, x
        res = 0
        while l <= r:
            mid = (l+r) // 2
            if mid**2 <= x:
                res = mid
                l = mid + 1
            else:
                r = mid -1
        return res
