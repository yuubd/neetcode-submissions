class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        Create the freq counter for the shorter string.
        using sliding window on the longer st, 
        compare the frequency map by each move,
        return true if match, false if loop finishes
        '''
        # alp_idx_m = {
        #     'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,
        #     'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,
        #     'u':20,'v':21, 'w':22,'x':23,'y':24,'z':25,
        # }
        # ... use ord(c)
        S, L = s1, s2
        if len(s2) < len(s1):
            return False

        c_s = [0] * 26
        for c in S:
            c_s[ord(c) - ord('a')] += 1

        l_s = [0] * 26
        l,r = 0, 0
        while r < len(L):
            l_s[ord(L[r]) - ord('a')] += 1
            
            if r - l == len(S):
                l_s[ord(L[l])-ord('a')] -= 1
                l += 1
                
            # if window len is same as the len of S, see found the answer
            if r - l + 1 == len(S) and c_s == l_s:
                return True

            
            
            r += 1

        return False

        
