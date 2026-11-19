class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        8:31
        1. For each height, we scan the whole heights again.
        2. Compare the vertical rectangle by itself, and look at the height of next heights, and time min * the len of heights - i the current index
        n = len of heights then O(n^2)

        [7,1,7,2,2,4]
        for i = 0 to len of heights
            for j from i to len of heights
                we have max(7(j-i+1)* min(heights[i:j+1])
        so for 
            i = 0
                7 2 3 4 5 6 => 7
            i = 1
                1 2 3 4 5 => 5
            i = 2
                7 4 5 8 => 8
            i = 3
                2 4 6 => 6
            i = 4
                2 4 => 4
            i = 5
                4 => 4
            ==> 8 
        
        Intuition: a rectangle must have a height and a bar is the height. 
        And the area is the height * r(the right bound) - l(leftbound) -1.

        Is a hiehgt is the height? Maybe. So put that in the stack.
        If next bar has smaller height, thats when the right bound is set.
        Before adding the smaller bar's idx, use it as right bound, 
            pop from the stack = thats the height that we will compute now.
            the st[-1] is the left bound as we know it s lower than the popped one.
            area = (smaller bar's indx - st[-1]'s idx - 1) * height of the popped idx
            do it while st[-1]'s height is higher than the smaller bar.
        when no bar on the stack, l = -1 if no more bar on the list, r = 0

        State:
        stack = holds unfinished bars' indexes
        maxArea = max area so far

        2 4 2 1 1 5 6
        '''

        maxArea = 0
        st = []
        r = 0
        heights.append(0)
        while r < len(heights):
            while st and heights[st[-1]] > heights[r]: # 7 > 1
                h = st.pop() # 0
                l = st[-1] if st else -1 # -1
                area = heights[h] * (r - l - 1) # 7 * (1 - -1 )
                maxArea = max(maxArea, area)
            
            st.append(r)
            r += 1
        '''
        st = [0 
        '''
        return maxArea






        






