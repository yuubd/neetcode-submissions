class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def is_palindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        res = []
        path = []

        def backtrack(start): # how to recognize we only need start as a param
            if start == len(s):
                res.append(path.copy())
                return

            for end in range(start, len(s)):
                if not is_palindrome(start, end):
                    continue
                path.append(s[start:end+1])
                backtrack(end+1) # try with the rest substring
                path.pop()

        
        backtrack(0)
        return res









