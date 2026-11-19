class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        '''
        states
            1. output is [0] * len num1 + num2
            2. carryOver 
            3. pos: idx of the next num in output

        length = len(output)
        pos = 0
        carryOver = 0
        for i from end of num1 
            for j from end of num2
                pos = i + j - 1
                productWithCarry = int num1[i] * int num2[j] + carryover
                digit = productWithCarry % 10
                carryover = productWithCarry // 10
                outpus[pos] += digit
        ret output
        12
        ^
        34
         ^
        i.     1 1 0. 0
        j.     1 0 1. 0
        pos.   3 2 2. 1
        pwCry. 8 6 10 4
        dgt.   8 6 0  4
        carry. 0 0 1. 0
        out   [0,4,0,8]

        '''
        
        output = [0] * (len(num1) + len(num2))
        carry = 0

        for i in range(len(num1)-1, -1, -1):
            pos = 0
            carry = 0
            for j in range(len(num2)-1, -1, -1):
                pos = i+j+1
                productWithCarry = int(num1[i]) * int(num2[j]) + carry + output[pos]
                # print(productWithCarry, pos)
                digit = productWithCarry % 10
                carry = productWithCarry // 10
                output[pos] = digit
            if carry:
                output[pos-1] = carry

        
        output[0] = carry
        output = [str(i) for i in output]
        res = ''.join(output).lstrip('0')
        return res if res else '0'
