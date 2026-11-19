class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        while l < r:
            if mid num is targe => return mid idx
            find the sorted area.
            If left side is sorted,
              if the target is on the left side, move r
              else move l
            If right side is sorted,
              do the same as above
        return -1
        '''

        l=0
        r=len(nums)-1

        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target: return mid

            if nums[l] <= nums[mid]: # left is sorted
                if nums[l] <= target < nums[mid]:
                    r = mid -1
                else:
                    l = mid +1
            else: # right is sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid -1
        return -1










    def search1(self, nums: List[int], target: int) -> int:
        '''
        find the min and run the BS
        '''

        l = 0
        r = len(nums) - 1
        min_n = nums[0]
        min_idx = 0
        count = 10
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < min_n:
                min_n = nums[mid]
                min_idx = mid
            print(l, mid, r)
            if nums[l] <= nums[mid] and nums[mid] <= nums[r]:
                if nums[l] < min_n:
                    min_n = nums[l]
                    min_idx = l    
                break
            if nums[mid] <= nums[r] <= nums[l]:
                r = mid - 1 # move left
            elif nums[r] <= nums[l] <= nums[mid]:
                l = mid + 1 # move right
            count -= 1
            if count == 0: break
            
        print("min_n",min_n, "min_idx",min_idx)

        l = 0
        r = len(nums) - 1
        rotates = min_idx
        count=10
        while l <= r:
            rotated_l = (l+rotates) % len(nums)
            rotated_r = (r+rotates) % len(nums)
            rotated_mid = ((rotated_l+rotated_r)) // 2
            print('l',l,'r',r, rotated_l, rotated_r, rotated_mid, "l+r+rotates//2", ((rotated_l+rotated_r) % len(nums)) // 2)

            if target == nums[rotated_mid]:
                return rotated_mid
            if target < nums[rotated_mid]:
                r = ((l+r) // 2) - 1
            if nums[rotated_mid] < target:
                l = ((l+r) // 2) + 1
            count -= 1
            if count == 0: break

        return -1





