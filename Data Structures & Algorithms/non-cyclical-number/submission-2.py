class Solution:
    def isHappy(self, n: int) -> bool:
        slow = self.getNextNum(n)
        fast = self.getNextNum(self.getNextNum(n))
        while slow != fast:
            slow = self.getNextNum(slow)
            fast = self.getNextNum(self.getNextNum(fast))
            if slow == 1: 
                return True
        
        return False if slow != 1 else True

    def getNextNum(self, n):
        # square all digits and return the sum
        ssum = 0
        while n > 0:
            ssum += int(n % 10) ** 2
            n //= 10
        return ssum




    def isHappy2(self, n: int) -> bool:    
        visited = set()
        ssum = 0
        num = n
        while True:
            while num > 0:
                ssum += int(num % 10)**2
                num //= 10
            if ssum == 1:
                return True
            if ssum in visited:
                return False
            visited.add(ssum)
            num = ssum
            ssum = 0
            
        return False