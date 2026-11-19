class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        '''
        BF: try every combination.
            for 2,4,3,1
            Alice picks           2                 24         243
            Bob picks      4     43.    431.     3.     31.     1
            Alice picks. 3  31    1              1                 
            Bob picks.   1
                      2+3 vs 4+1 = diff is 0
            time = O(3^n) cuz max three choices per node and there are n depth
            space = O(n) n many recursion stack

            2 A 
            |
            4 B
            
            2 4  A
            |
            None B

            so dfs(i) represent the max diff in val at i 
            dfs(i) is the maximum score difference the current player can achieve over the other player using stones from index i onward.
            base 
                if i == n (len of stonValue) meaning no more stone. the diff is 0,
                return 0 cuz we cant pick the stone
                # we need the max of the diff. Apply it to the base case above. It works perfectly
                pickOne = sum(stoneValue[i:i+1]) - dfs(i+1) if i + 1 <= n else 0
                pickTwo = sum(stoneValue[i:i+2]) - dfs(i+2) if i + 2 <= n else 0
                pickThree = sum(stoneValue[i:i+3]) - dfs(i+3) if i + 3 <= n else 0
                return max(pickOne, pickTwo, pickThree)
        memo:
            time: O(n) once we populate the cache, each dfs is constant call
            space: O(n) recursion stack and cache
        DP:
            This we cant go from beginning to n but n to 0 cuz when we want the diff at i, we need the diff when taking after i:i+1, i:i+2, i:i+3. Backwards could work but doesnt make sense,..
            time: O(n) we are building the cache from n-1 to 0 and it s a one run with accessing the cache
            space: O(n) the cache, but we can optimize it to O(3) we only need to keep the three

        '''
        n = len(stoneValue)
        
        # DP with space O(3)
        cache = deque([0] * 3)
        for i in range(n-1, -1, -1): 
            diffAfOne   = sum(stoneValue[i:i+1]) - cache[0] if i+1 <= n else -float("inf")
            diffAfTwo   = sum(stoneValue[i:i+2]) - cache[1] if i+2 <= n else -float("inf")
            diffAfThree = sum(stoneValue[i:i+3]) - cache[2] if i+3 <= n else -float("inf")
            
            cache.appendleft(max(diffAfOne, diffAfTwo, diffAfThree))
            cache.pop()

        if  cache[0] > 0:
            return "Alice"
        if  cache[0] < 0:
            return "Bob"
        return "Tie"

        # DP
        cache = {n: 0}
        for i in range(n-1, -1, -1): 
            diffAfOne   = sum(stoneValue[i:i+1]) - cache[i+1] if i+1 <= n else -math.inf
            diffAfTwo   = sum(stoneValue[i:i+2]) - cache[i+2] if i+2 <= n else -math.inf
            diffAfThree = sum(stoneValue[i:i+3]) - cache[i+3] if i+3 <= n else -math.inf
            
            cache[i] = max(diffAfOne, diffAfTwo, diffAfThree)

        if  cache[0] > 0:
            return "Alice"
        if  cache[0] < 0:
            return "Bob"
        return "Tie"


        cache = {}
        def dfs(i):
            if i == n:
                return 0
            if i in cache:
                return cache[i]

            pickOne = sum(stoneValue[i:i+1]) - dfs(i+1) if i + 1 <= n else float("-inf")
            pickTwo = sum(stoneValue[i:i+2]) - dfs(i+2) if i + 2 <= n else float("-inf")
            pickThree = sum(stoneValue[i:i+3]) - dfs(i+3) if i + 3 <= n else float("-inf")
            # print("i", i, "diff", max(pickOne, pickTwo, pickThree))
            cache[i] = max(pickOne, pickTwo, pickThree)
            return cache[i]
        
        diff = dfs(0)
        if diff > 0:
            return "Alice"
        if diff < 0:
            return "Bob"
        return "Tie"




