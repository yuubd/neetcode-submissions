class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        same number of chars in both 
        base cases
        s=s t=t false
        s=s t=s true
        s=s t=sss false => length are same
        '''
        if len(s) != len(t):
            return False
        s_dict = defaultdict(int)
        for char in s:
            s_dict[char] += 1
        for char in t:
            s_dict[char] -= 1
            if s_dict[char] == 0:
                del s_dict[char]
    
        return len(s_dict) == 0