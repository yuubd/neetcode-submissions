class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        subset = []
        def backtracking(i, total):
            if total == target:
                res.append(subset.copy())
                return
    
            if i == len(candidates) or total > target:
                return
                
            subset.append(candidates[i])
            backtracking(i+1, total + candidates[i])
            subset.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtracking(i+1, total)
        
        backtracking(0, 0)
        return res