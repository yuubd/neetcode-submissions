class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        idxes = defaultdict(int)
        for i, char in enumerate(order):
            idxes[char] = i
        print(idxes)
        def inOrder(wrd1, wrd2):
            for ch1, ch2 in zip(wrd1, wrd2):
                if idxes[ch1] == idxes[ch2]:
                    continue
                if idxes[ch1] < idxes[ch2]:
                    return True
                else:
                    return False

            return True if len(wrd1) <= len(wrd2) else False
    
        prev = words[0]
        for curr in words[1:]:
            if not inOrder(prev, curr):
                return False
            prev = curr
        return True
        
        