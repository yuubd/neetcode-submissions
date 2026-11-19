class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        if s == t:
            return s

        res_l, res_r = 0, math.inf
        missing = len(t)
        counter = Counter(t)
        
        l = r = 0
        while r < len(s):
            # print(counter)
            # add s[r]
            char = s[r]
            # print(char, r)
            if char in counter:
                counter[char] -= 1
                if counter[char] >= 0:
                    missing -= 1
            
            while missing == 0:
                # print("l r",l, r)
                if r-l < res_r-res_l:
                    res_l, res_r = l, r 
                
                char = s[l]
                if char in counter:
                    counter[char] += 1
                    if counter[char] > 0:
                        missing +=1
                l += 1
            r += 1
            # print(l,r)
            
        return s[res_l:res_r+1] if res_r != math.inf else ""