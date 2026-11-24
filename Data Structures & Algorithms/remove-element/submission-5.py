class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        two pointers

        starting from the beginning to end

        if encounters the val, replace with the non val equal from r

        '''


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



        