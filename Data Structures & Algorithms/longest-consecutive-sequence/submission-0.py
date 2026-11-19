class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        set 
        find the tail if n - 1 doesnt exsit, its tail,
        when find tail, increment and find the head and save the count,
        do it until the end.
        The non tail numbers will be skipped anyways.
        '''

        max_c = 0
        s = set(nums)
        for n in nums:
            if n-1 not in s:
                next = n+1
                curr_max = 1
                while next in s:
                    curr_max += 1
                    next += 1 
                max_c = max(max_c, curr_max)
        return max_c


