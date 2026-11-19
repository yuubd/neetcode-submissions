class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -float("inf")
        curr_max = 0
        for n in nums:
            curr_max += n
            res = max(res, curr_max)
            if curr_max < 0:
                curr_max = 0
            print(curr_max)
        return res