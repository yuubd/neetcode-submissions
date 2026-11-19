class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)
        def backtracking(perm, used):
            if len(perm) == len(nums):
                res.append(perm.copy())
            
            for i in range(len(nums)):
                if used[i] == True: # meaning we have added this in perm
                    continue
                
                used[i] = True
                perm.append(nums[i])
                backtracking(perm, used)
                perm.pop()
                used[i] = False

        backtracking([], used)
        return res

                