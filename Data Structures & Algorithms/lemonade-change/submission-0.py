class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        '''
        counter for each bill
        if 5, just increment 5
        if 10, increment 10 and decrement 5
        if 20, increment 20, decrement one ten one five or three fives

        if any of them are false,
        return false
        '''

        counter = defaultdict(int)

        for bill in bills:
            if bill == 5:
                counter[5] += 1 
            elif bill == 10:
                if counter[5] < 1:
                    return False
                counter[5] -= 1
                counter[10] += 1
            elif bill == 20:
                if counter[5] >= 1 and counter[10] >= 1:
                    counter[5] -= 1
                    counter[10] -= 1
                    counter[20] += 1
                elif counter[5] >= 3:
                    counter[5] -= 3
                    counter[20] += 1
                else:
                    return False
        return True