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

            When i = len n -1 or capacity == 0 return valueSum
            decision1: skip picking ith item. By recurse on i + 1 with same capacity, valueSum
            decision2: include the ith item, 
                       so recurse on i + 1 with cap + ith capacitt, valueSum + ith value
            
            return the max of two decisions
        '''
        n = len(profit)
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
