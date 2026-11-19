class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        '''
        we need a counter of 1 and 0 for a str

        BF: try all combinations
            at each, we have two branches as we can include or not and len of strs depth
            time: O(2^n)
            space O(n) for recursion
            dfs(i)
                if i == len strs: meaning we dont have no more str to add
                    return 0
                skip = dfs(i+1, remainingN, remaining M)
                nInStr, mInStr = get n and m of str
                
                include = -math.inf # or 0 works as the answer >= 0 / # when invalid
                if remainingN-nInStr >= 0 and remaining M - MInStr >= 0:
                    include = dfs(i+1, remainingN-nInStr, remaining M - MInStr)
                return max(skip, include)
        Memo:
            we can add cache where cache[i] is the max # of subset from ith onwards with m and n

        '''

        zerosAndOnes = []
        for idx, s in enumerate(strs):
            zeros, ones = strs[idx].count("0"), strs[idx].count("1")
            zerosAndOnes.append((zeros, ones))

        cache = {}
        def dfs(i, rZeros, rOnes):
            if i == len(strs):
                return 0
            
            if (i, rZeros, rOnes) in cache:
                return cache[(i, rZeros, rOnes)]

            skip = dfs(i+1, rZeros, rOnes)
            include = -math.inf
            zeros, ones = zerosAndOnes[i]
            if rZeros - zeros >= 0 and rOnes - ones >= 0:
                include = 1 + dfs(i+1, rZeros - zeros, rOnes - ones)
            cache[(i, rZeros, rOnes)] = max(skip, include)
            return cache[(i, rZeros, rOnes)]
        
        return dfs(0, m, n)
