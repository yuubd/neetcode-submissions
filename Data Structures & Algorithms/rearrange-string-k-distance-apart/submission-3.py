class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        counter = Counter(s)
        print(counter)
        # is a (count * k) + 1 <= len(s) ret ""
        '''
        asdasda
        k=2
        a=3
        s=2
        d=2
        n=7
        '''
        
        cooling = [] # time, count, char
        free = [[-counts, char] for char, counts in counter.items()] # count, char
        heapq.heapify(free)
        res = [""] * len(s)
        curtime = 0
        while free or cooling:
            while cooling and cooling[0][0] <= curtime:
                t, c, ch = heapq.heappop(cooling)
                heapq.heappush(free, [c, ch])
            
            if len(free) == 0:
                return ""
            
            counts, char = heapq.heappop(free)

            res.append(char) # res = a s a d a s d 
            if counts != -1:
                heapq.heappush(cooling, [curtime+k, counts+1, char])
            curtime += 1
            
        return "".join(res)



