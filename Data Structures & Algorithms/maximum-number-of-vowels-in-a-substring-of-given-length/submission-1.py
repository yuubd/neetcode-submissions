class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        '''
        BF: for each sub string, check the vowel count
        states:
        maxCount
        asdasd 5 len = 6 k = 3
        O(n*k)

        need a prefix of vowel counts and count = prefix[l+r] - prefix[l+1]

        '''
        vowels = set(["a","e","i","o","u"])
        vowelPrefix = [0] * (len(s)+1)
        for i, char in enumerate(s):
            vowelPrefix[i+1] = (1 if char in vowels else 0) + vowelPrefix[i]
        
        maxCount = 0
        for i in range(0, len(s)-k+1):
            count = vowelPrefix[i+k] - vowelPrefix[i]
            maxCount = max(maxCount, count)
        return maxCount




