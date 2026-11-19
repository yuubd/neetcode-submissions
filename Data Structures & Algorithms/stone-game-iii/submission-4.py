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
            base 
                if i == n (len of stonValue) meaning no more stone. the diff is 0,
                return 0 cuz we cant pick the stone
                # we need the max of the diff. Apply it to the base case above. It works perfectly
                pickOne = sum(stoneValue[i:i+1]) - dfs(i+1) if i + 1 <= n else 0
                pickTwo = sum(stoneValue[i:i+2]) - dfs(i+2) if i + 2 <= n else 0
                pickThree = sum(stoneValue[i:i+3]) - dfs(i+3) if i + 3 <= n else 0
                return max(pickOne, pickTwo, pickThree)
        '''
        n = len(stoneValue)
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




