class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        '''
        The brute force is trying every combination:
        n = len(nums)
        1=1
        2=2
        3=6
        4=24
        5=120 n!
        O(n!)


        1. dp[l][r] = the money we can get from nums[l:r] so starting will be dfs(0, len(nums)-1)
            because the variable here is the size of the remaining.
        2. base: l<r(so the len) == 0: ret 0
        3. nums[l-1]*nums[k]*nums[r+1] << this is like we will pop nums[k] at the LAST in range l:r meaning there is no number in ther range except for at kth. nums[k] will be multiplied with outer numbers from each side
        '''
        nums = [1] + nums + [1]
        dp = {}
        def dfs(l, r):
            if r < l: return 0
            if (l,r) in dp:
                return dp[(l, r)]
            
            best = 0
            for k in range(l, r+1):
                best = max(best, dfs(k+1, r) + nums[l-1]*nums[k]*nums[r+1] + dfs(l, k-1))
            dp[(l, r)] = best
            return dp[(l, r)]
        
        return dfs(1, len(nums)-2)
