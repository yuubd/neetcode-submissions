class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        n mod 10 will give the last digit append to a list and a visited set
        then // 10 
        repeat until n = 0

        sum = 0
        for each n in the list,
            sum += n^2
        if sum is 1: return true
        if sume is in visited, return false
        '''
        
        visited = set()
        ssum = 0
        num = n
        while True:
            while num > 0:
                print(int(num % 10), num//10)
                ssum += int(num % 10)**2
                num //= 10
            print('ssum', ssum)
            if ssum == 1:
                return True
            if ssum in visited:
                return False
            visited.add(ssum)
            num = ssum
            ssum = 0
            
        return False