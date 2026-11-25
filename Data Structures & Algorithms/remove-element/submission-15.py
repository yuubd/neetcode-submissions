class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        two pointers

        starting from the beginning to end

        if encounters the val, replace with the non val equal from r

        when r = len n -1
        l <= r
        3 3.      2
        l r 1 0

        when r = len n
        l < r
        3 3
        l r 1 1

        when r = len n
        l <= r
        3 3      2
        l r 1 1
        '''
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] == val:
                nums[l] = nums[r]
                r -= 1
            else:
                l += 1
        return l


        l, r = 0, len(nums)-1
        
        k = sum(n != val for n in nums)
        
        l, r = 0, k
        while l < k:
            if nums[l] == val:
                while nums[r] == val:
                    r += 1
                nums[l], nums[r] = nums[r], nums[l]
            l += 1
        return k



        