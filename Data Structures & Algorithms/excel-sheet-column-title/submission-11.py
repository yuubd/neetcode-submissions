class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        numToStr = {i: chr(ord("A") + i) for i in range(26)}


        '''
        26^X

        53 => BA 
        > 26^0
        > 26^1
        < 26^2


        53 // 26 = 2 => B
        53 % 26 = 53/52 = 1 => A

        get X, do division and then modulo
        '''

        res = []
        while columnNumber > 0:
            columnNumber -= 1
            cur = columnNumber % 26
            print(cur, numToStr[cur], columnNumber // 26)
            res.append(numToStr[cur])
            columnNumber //= 26
        return "".join(reversed(res))

        
        





