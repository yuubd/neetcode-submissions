class Solution:
    def reverse(self, x: int) -> int:
        '''
        0000 0000 0000 1000 = 8  => 8  = 0000 0000 0000 1000
        0000 0000 0000 1100 = 12 => 21 = 0000 0000 0001 0101
        0000 0000 0000 1010 = 10 =>  1 = 0000 0000 0000 0001

        Ther is no pattern here.
        Decimal replacement maybe.
        123 = > 321
        3 * 100 + 2 * 10 + 1*1

        base = 1*10 while number is > 0?
        while the number is > 0:
            we need the last digit and multiply with the base.
            digit is % 10 
            // 10 will make it 1/10
            res += base * digit
            base = // 10
        return res
        '''

        res = 0
        base = 1
        tmp = x if x >= 0 else -x
        while tmp >= 10:
            base *= 10
            tmp //= 10
        print("base", base)

        tmp = x if x >= 0 else -x
        while tmp > 0:
            '''
            x   = 123. 12.  1
            res = 4000 4300 432
            '''
            digit = tmp % 10
            tmp //= 10
            res += base * digit
            base //= 10
        
        if not (-2**31 <= res <= 2**31 - 1):
            return 0

        return res if x >= 0 else -res






