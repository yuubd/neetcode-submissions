class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''
        we can do normal combination and then only choose the k length ones
        instead of making a list from 1 to n, also I can pass 0 + 1 until it s n

        states:
            combs
            comb

            dfs 
                if the comb len == k, copy and append and return    
                try with appending curr num 
                pop and try skipping
            
            return the combs
        '''

        combs = []
        def dfs(i, comb):
            if len(comb) == k:
                combs.append(comb)
                return
            
            if i < n:
                dfs(i+1, comb+[i+1])
                dfs(i+1, comb)
            

        dfs(0, [])
        return combs

