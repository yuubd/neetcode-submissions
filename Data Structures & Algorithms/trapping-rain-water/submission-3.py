class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l, r = 0, len(height)-1
        l_max, r_max = 0,0
        while l < r:
            l_max = max(l_max, height[l])
            water += l_max - height[l]
            r_max = max(r_max, height[r])
            water += r_max - height[r]
            if l_max < r_max:
                l += 1
                # l_max = max(l_max, height[l])
                # water += l_max - height[l]
            else:
                r -= 1
                # r_max = max(r_max, height[r])
                # water += r_max - height[r]
        return water












    def trap2(self, height: List[int]) -> int:
        '''
        This can be done by prefix and postfix array 
            which stores the higher bar.
        And then on the other loop at ith posistion the amount the col
            contain is the min of the pre and post max bar - the bar height 
            of the current potition.
        It works because the max on left or right side is the potential max
            raindrop. But meanwhile comparing the two the drop only can be hold
            up to the min of two max.
        '''
        if len(height) <= 2: return 0

        res = 0
        l_max_bars = [0] * len(height)
        r_max_bars = [0] * len(height)

        curr_max = height[0]
        for i in range(1, len(height)):
            curr_max = max(curr_max, height[i-1])
            l_max_bars[i] = curr_max
        print(l_max_bars)            

        curr_max = height[len(height)-1]
        for i in range(len(height)-2, -1, -1):
            curr_max = max(curr_max, height[i+1])
            r_max_bars[i] = curr_max
        print(r_max_bars)            
        print(height)

        for i in range(len(height)):
            res += max(min(l_max_bars[i], r_max_bars[i]) - height[i], 0)
        
        return res











        


