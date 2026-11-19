class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def backtracking(i, total):
            if sum(subset) == target:
                res.append(subset.copy())
                return
    
            if i == len(nums) or total > target:
                return
                
            subset.append(nums[i])
            backtracking(i, total + nums[i])
            
            subset.pop()
            backtracking(i+1, total)
        
        backtracking(0, 0)
        return res