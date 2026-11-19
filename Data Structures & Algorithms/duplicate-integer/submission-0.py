class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        create a set. if found, return true, not, return false.
        '''
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False