class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        '''
        3:06 -> 3:22 but not the answer

        1 2 3 
        1 3   -1 * 2
        2     -1 * 2

        1 2 3 -2 * 2
        1 1   -1 * 2 
        0

        So we smash stones with higher to lower

        bf = try all paths and keep the largest
        time: O(n!)
        space: O(n) recursion stack

        [1 2]
        
        [].     [1 2]
        [1].    [2]
        [1 2].  []
        We can know the half from sum(stones) // 2 

        states:
            half = sum(stones) // 2 
            def dfs(i, bag):
                if i == n: we have looked at all stones at the end leave
                    return sum(bag) - half
                
                include = dfs(i+1, bag + stones[i])
                skip = dfs(i+1, bag)
                
                rerurn min(skip, include)
            return dfs(0, [])
        
        

        more optimal using max heap
        store all stones in the heap
        while the len > 1:
            pick two largest, 
            if equal, continue,
            comput the new stone and push to the heap
        return the remaining
        '''

        '''
        [4,4,1,7,10]
        [-10, -7, -4, -4, -1]

        -4 -4 -3 -1
        -3 -1
        -2

        nah.. we need to try all combinations with memo...
        There is no pattern. 
        The only pattern we know is we want to minimize the diff between two bags of stones
        cuz the answer is abs(bagA - bagB)
        
        so
        dp[i] = 
        if i == n: # there are no moer stones
            return nothing

        for each stone
            try with the stone at i
            try skip (adding it to the other bag)

        '''

        n = len(stones)
        whole = sum(stones) 
        half = whole // 2 
        cache = {}
        






        cache = {}
        def dfs(i, bagSum):
            if i == n: # we have looked at all stones at the end leave
                bagBSum = whole - bagSum
                return abs(bagBSum - bagSum)
            
            if (i, bagSum) in cache:
                return cache[(i, bagSum)]
            
            include = dfs(i+1, bagSum + stones[i])
            skip = dfs(i+1, bagSum)
            cache[i, bagSum] = min(skip, include)

            return cache[i, bagSum]
        
        return dfs(0, 0)






















        