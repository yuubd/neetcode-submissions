class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        Get the max val
        if h == len(piles) => return the largest in the list
        try with the mid of the max val and run BS to find the output
        '''
        max_p = max(piles)

        min_rate = 1
        max_rate = max_p
        sum_h = 0 
        res_rate = 0
        while min_rate <= max_rate: # l <= r is the rule
            curr_rate = (min_rate+max_rate) // 2
            
            sum_h = 0
            for p in piles:
                sum_h += math.ceil(p/curr_rate)
            print("curr_rate", curr_rate, "min_rate", min_rate, "max_rate", max_rate, "res_rate", res_rate, "sum_h", sum_h)            
            if sum_h <= h: # meaning the rate is small enough chekc if there are any smaller one. So no need to min 
                res_rate = curr_rate
                max_rate = curr_rate - 1 # r = curr - 1 rule 2
            else:
                min_rate = curr_rate + 1 # l = curr + 1 rule 3

        return res_rate


