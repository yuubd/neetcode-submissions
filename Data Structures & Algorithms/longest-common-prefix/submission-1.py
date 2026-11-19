class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        9:49
        BF: scan all words by index, 
        check each character, 
        if one is different, 
        return "" 
        after one scan, append the ith char

        
        pick a word, compare the work to the next, only leave the common
        keep doing it until the end
        '''

        word = strs[0]
        for nextWord in strs[1:]:
            for i in range(len(word)):
                if i >= len(nextWord) or word[i] != nextWord[i]:
                    word = word[:i]
                    break
        return word

        


