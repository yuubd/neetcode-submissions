class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        '''
        It s 0/1 knapsack cuz we have choices of keeping or not keeping an item.
        Greedy would not work because the weights might become a bootleneck.
            eg. there is an item with profit of 10 and weight of 8 
            and two more items with profit of 6 with weight of 4 each and capacity of 8. 
            Skipping the first and picking up the second and third is the optimal.
            Meaning we need to try all combination of skip and take it.

        BF:
            It can be represented as a decision tree of 2.
            At i, we have two choices(pick up or not).
            The depth is as many as n as we move i one by one and make decisions

            We have a decision tree.
            Starting at i = 0, we traverse to the leaf nodes and return the totalValue.
            Only track of the max value.

            When i = len n -1 return 0
            decision1: skip picking ith item. By recurse on i + 1 with same capacity, valueSum
            decision2: include the ith item, if capacity-capacity at i >= 0
                       recurse on i + 1 with cap + ith capacitt, valueSum + ith value
                       0 othewise (picking up the curr item will exceeds the capacity)
            
            return the max of two decisions
            time: O(2^n) as the tree has 2 choices at i and n depth
            space: O(n) for recursion stack
        
        Memo:
            We can optimize it with using cache becuase the tree has lots of duplications.
            We want the profit of items from ith onwards with capacity c, 
            so we can cache the profit of items with capacity c

        DP:
            cache[i][c] = the profit at items[:i] with remaining capacity c
            cache[i][0] = when no capacity, then 0
            cache[0][c] = when with only first item, it s profit[i] when weight[i] >= c

            cache[i][c] = max of skip and include ith item
                    skip = cache[i-1][c] try carrying the max profit at i - 1 and 
                    include = profit[i] + cache[i-1][c-weight[i]] if c - weight[i] >= 0 else 0
            return cache[n][capacity]
        '''
        n = len(profit)

        cache = [0] * (capacity+1)
        for c in range(capacity+1):
            cache[c] = profit[0] if c - weight[0] >= 0 else 0

        for i in range(1, n):
            tmpCache = [0] * (capacity+1)
            for c in range(1, capacity + 1):
                skip = cache[c]
                include = profit[i] + cache[c-weight[i]] if c-weight[i] >= 0 else 0
                tmpCache[c] = max(skip, include)
            cache = tmpCache
        return cache[capacity]

        # Bottom-up: cache[(i, c)] stores the maximum profit obtainable using items from index 0 through index i with capacity c.
        cache = {}
        # base cases
        for i in range(n):
            # when capacity is 0, 0 profit
            cache[(i, 0)] = 0
        for c in range(capacity+1): # capacity 0 to full capacity
            # when with one item, profit of i or 0 depending on c
            cache[(0, c)] = profit[0] if c - weight[i] <= 0 else 0

        for i in range(1, n):
            for c in range(1, capacity + 1):
                skip = cache[(i-1, c)]
                include = profit[i] + cache[(i-1, c-weight[i])] if c-weight[i] >= 0 else 0
                cache[(i, c)] = max(skip, include)
        return cache[(n-1, capacity)] # using all items at full capacity



        # Top-down: cache[(i, c)] stores the maximum profit obtainable using items from index i onward with capacity c.
        cache = {}
        def dfs(i, remainingCapacity):
            if i == n:
                return 0
            if (i, remainingCapacity) in cache:
                return cache[(i, remainingCapacity)]

            skip = dfs(i+1, remainingCapacity)
            newCapacity = remainingCapacity-weight[i]
            include = profit[i] + dfs(i+1, newCapacity) if newCapacity >= 0 else 0
            cache[(i, remainingCapacity)] = max(skip, include)
            return cache[(i, remainingCapacity)]

        return dfs(0, capacity)
