class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        '''
        one of them must be a substring of another to have a common divisor
        find the smaller one and find the pattern

        len of larger str % some samller[:i] == 0
        check largerStr starts with samller[:i]
        if yes, return
        after loop, ""
        '''
        if str1[0] != str2[0]:
            return ""

        smaller, larger = (str2, str1) if str1.startswith(str2) else (str1, str2)
        
        print(smaller, larger)
        candidates = []
        for i in range(len(smaller), 0, -1):
            if len(larger) % len(smaller[:i]) == 0 and len(smaller) % len(smaller[:i]) == 0:
                found = True
                for j in range(0, len(larger), i):
                    if larger[j:j+i] != smaller[:i]:
                        found = False
                
                if found:
                    return smaller[:i]
                    candidates.append(smaller[:i].copy())
            


        return ""