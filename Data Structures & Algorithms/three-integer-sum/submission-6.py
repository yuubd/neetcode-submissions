class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res =[]
        nums.sort()
        for i, n in enumerate(nums):
            l, r = i+1, len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1 # cuz we found from l and r and no duplicate

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1

        return res