class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
            9:55
            s = abab
            p = ab
            ret [0, 1, 2]

            s=asdfgffasd
            p=asd
            ret [0, 7]

            sliding window
            states
                l, r, the size is r-l+1
                p's connter
                res = [] list of indices
                starting from l r 0 and is size is less than the len of p, keep increase
                while increasing, we need to keep track of a counter(an array of len of 26(alphabets))
                if equals to p's connter, add the idx to res,
                move one by one until r >= len(s)
            ret res
        '''

        if len(p) > len(s):
            return []
        
        counterP = [0] * 26
        for char in p:
            counterP[ord(char) - ord('a')] += 1
        # print(counterP)
        
        l = r = 0
        counter = [0] * 26
        res = []
        while r < len(s):
            char = s[r]
            counter[ord(char) - ord('a')] += 1
            if r-l+1 < len(p):
                r += 1
                continue
            # print(counter)
            # check the anagram
            if counter == counterP:
                res.append(l)
            
            # remove l before moving window
            char = s[l]
            counter[ord(char) - ord('a')] -= 1
            l += 1
            r += 1



        return res
        
