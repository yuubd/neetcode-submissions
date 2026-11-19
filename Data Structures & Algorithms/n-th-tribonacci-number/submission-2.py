class Solution:
    def tribonacci(self, n: int) -> int:
        '''
        11:26
        DP
            dp is list of len of n.
            base cases: when T0 = 0, T1 = 1, T2 = 1
            else is Tn+3 = Tn + Tn+1 + Tn+2
            return the last
        '''
        if n == 0:
            return 0
        if n < 3:
            return 1

        cache = [0] * 3
        cache[1] = cache[2] = 1
        cache = deque(cache)
        
        
        for i in range(3, n+1):
            cache.append(cache[2] + cache[1] + cache[0])
            cache.popleft()
        return cache[2]
