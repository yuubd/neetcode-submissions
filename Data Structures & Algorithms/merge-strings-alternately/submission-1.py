class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        res = []        
        for ch1, ch2 in zip(word1, word2):
            res.append(ch1)
            res.append(ch2)

        idx = min(len(word1), len(word2))
        
        if len(word1) <= len(word2):
            res.append(word2[len(word1):])
        else:
            res.append(word1[len(word2):])
        
        return "".join(res)
        

