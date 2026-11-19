class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        It s sorted.
        Staring with two ptrs. l and r.
        l from 0 ++
        r from len(nums) --
        if sum == t, return
        if the sum < target => increase l
        otherwise decrease r

        stop when l=r
        '''
        l = 0
        r = len(numbers)-1
        while l != r:
            tsum = numbers[l] + numbers[r]
            if tsum == target:
                return [l+1, r+1]
            if tsum < target:
                l += 1
            else:
                r -= 1
        return []

