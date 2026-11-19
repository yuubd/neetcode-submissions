class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        '''
        get a dict of char: idx
        in another loop add the index
        '''

        idxDict = defaultdict(int)
        for i, char in enumerate(keyboard):
            idxDict[char] = i
        
        total = 0
        i = 0
        for char in word:
            idx = idxDict[char]
            total += abs(i-idx)
            i = idx

        return total
