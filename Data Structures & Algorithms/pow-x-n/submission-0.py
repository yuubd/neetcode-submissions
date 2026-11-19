class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''
        n < 0 set a flag like isNegative True and 1/res when return
        n == 0: return -
        n > 0: for _ in range of n, just multiple x to x n time


        x^n = (x*x)^n/2 for even
        x^n = x(x*x)^n/2 for odd
        when n = 0 x^0 = 1
        when x = 0 0^n = n
        so res = myPowHelper(x*x, n//2)
        and if n % 2 == 1 return res * x else res
        '''

        def myPowHelper(x, n):
            if n == 0: return 1
            if x == 0: return 0

            res = myPowHelper(x*x, n//2)
            return res if n % 2 == 0 else res * x
 
        return myPowHelper(x, abs(n)) if n >= 0 else 1/myPowHelper(x, abs(n)) 

