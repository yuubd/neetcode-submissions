class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        from the nums, we can choose or not: 2 choices
        we would add all the leaf nodes from the tree
        we append the curr subset when the depth-1 is n

                  1 2
        i=0    []     1
        i=1  []   2  1  12
        i=2. add add add add
        '''

        subsets = []
        subset = []
        def dfs(i):
            if i == len(nums):
                subsets.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return subsets







































    def subsets2(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        def backtracking(i):
            if i == len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[i])
            backtracking(i+1)

            curr.pop()
            backtracking(i+1)

        backtracking(0)
        return res