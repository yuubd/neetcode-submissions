class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += "#"
            res += s
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        '''
        find the length which is index i to j where j is #
        when get the length, append the char to string length times
        repaet until j is out of the len(s)
        '''
        res = []
        l = 0
        r = 0
        while r < len(s):
            while s[r] != "#":
                r += 1
            leng = int(s[l:r])
            l = r + 1
            r += 1 + leng
            print("l:", l, "r:", r, "leng:", leng, "word:", s[l:r])
            res.append(s[l:r])
            l = r

        return res
