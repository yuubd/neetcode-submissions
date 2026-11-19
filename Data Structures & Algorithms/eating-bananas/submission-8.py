class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        Get the max val
        if h == len(piles) => return the largest in the list
        try with the mid of the max val and run BS to find the output
        '''

        max_p = 0
        for p in piles:
            max_p = max(max_p, p)
        print("max_p", max_p)

        min_rate = 1
        max_rate = max_p
        sum_h = 0 
        res_rate = 0
        while min_rate <= max_rate:
            curr_rate = (min_rate+max_rate) // 2
            print("curr_rate", curr_rate, "min_rate", min_rate, "max_rate", max_rate, "res_rate", res_rate, "sum_h", sum_h)
            sum_h = 0
            for p in piles:
                sum_h += math.ceil(p/curr_rate)
            
            if sum_h <= h:
                res_rate = curr_rate
                max_rate = curr_rate - 1
            else:
                min_rate = curr_rate + 1
            
                
            
        
        return res_rate


