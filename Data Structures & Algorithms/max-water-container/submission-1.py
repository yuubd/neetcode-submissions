class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        starting from both ends
        move one side (l)

        move smaller side until find "bigger" than prev
        calculate the water, compare

        until i < j

        return the max
        '''

        i = 0
        j = len(heights)-1
        max_amount = 0

        while i < j:
            h_1 = heights[i]
            h_2 = heights[j]

            amount = (j-i) * min(h_1, h_2)
            max_amount = max(amount, max_amount)
            # print("h_1", h_1, "h_2", h_2, "max_amount", max_amount)

            if h_1 < h_2:
                i += 1
            else:
                j -= 1
            
        return max_amount

            













