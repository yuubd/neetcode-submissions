class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''
        This is at each depth, there are n choices - used index
        base case: if the len of curr perm is same as nums len, append in the set

        perms = set()
        def dfs(i, perm, used):
            if perm len == n: append to perms copy()

            for i, n in nums enum:
                if i in used, continue
                add the n to perm and i to used
                dfs(newPerm and used)
                pop on newPerm only
        dfs(0,[],set[])
        return the perms
        '''

        n = len(nums)
        perms = set()
        def dfs(perm, used):
            if len(perm) == n:
                perms.add(tuple(perm.copy()))
                return
            
            for i, num in enumerate(nums):
                if i in used:
                    continue
                '''
                perm 1
                used 0

                perm 1 1, 1 2,
                used 0 1, 0 2,

                perm 1 1 2, 1 2 1
                used 0 1 2, 0 2 1
                '''
                used.add(i)
                perm.append(num)
                dfs(perm, used)

                perm.pop()
                used.remove(i)
        
        dfs([], set())
        return [list(perm) for perm in perms]










