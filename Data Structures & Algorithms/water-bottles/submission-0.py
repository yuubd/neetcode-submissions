class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        '''
        drunk = numBottles
        while numExchange <= left:
            left -= numBottles+1
            drunk += 1
        return drunk
        '''

        drunk = numBottles
        while numExchange <= numBottles:
            numBottles -= (numExchange)
            numBottles += 1
            drunk += 1
        return drunk
