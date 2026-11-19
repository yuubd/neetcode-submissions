class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        1. we should use the Bellman-Ford as we need to go over all edges and there is a limit to how many we can go
        2. minPrices arr in length of n the init val is inf with prices[src] = 0
        3. loop over the flights(edges) k + 1 many times 
        4. for each loop, the prices[dest] += cost
        5. if the flight[1] == dst: track the min and continue 
        6. return the global min
        '''
        prices = [math.inf] * n # we are keeping the min cost
        prices[src] = 0

        for _ in range(k+1):
            tmp_prices = prices.copy()
            for f, t, price in flights:
                if prices[f] > math.inf:
                    continue
                if prices[f] + price < tmp_prices[t]:
                    tmp_prices[t] = prices[f] + price
            prices = tmp_prices
        print(prices)
        return prices[dst] if prices[dst] != math.inf else -1