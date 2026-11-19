class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''
        if the last digit is not 9, add 1 to the last digit and return

        starting from the last idx to 0
        if 9, output[idx] = 0 and carry over = True
        until next num is not 9
        '''

        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits