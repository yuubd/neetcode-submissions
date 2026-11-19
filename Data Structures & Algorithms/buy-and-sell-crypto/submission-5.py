class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        We are looking for the biggest + in the price
        We want the max of any r - l
        4 base cases
        1. l=0 r=len(prices)-1
        2. 0<l r=len(prices)-1
        3. l=0 r<len(prices)-1
        4. 0<l r<len(prices)-1

        l < r

        if r-l <= 0: then l r move together by 1
        if 0 < r-l: increment r to find more profit
        if len(prices) < r: return the max
        '''
        l = r = 0
        profit = 0
        while r < len(prices):
            curr_profit = prices[r] - prices[l]
            if curr_profit < 0:
                l = r
            else:
                profit = max(curr_profit, profit)

                r += 1
        
        return profit
        