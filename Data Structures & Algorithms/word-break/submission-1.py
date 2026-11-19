class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[0] = True

        for i in range(1, len(s)+1):
            end = i
            for w in wordDict:
                start = end - len(w)
                if start < 0:
                    continue
                
                if s[start:end] == w:
                    if dp[start] == True:
                        dp[i] = dp[start]
                        break # break only when we found the correct word and all prefix is solvable

        return dp[len(s)]
