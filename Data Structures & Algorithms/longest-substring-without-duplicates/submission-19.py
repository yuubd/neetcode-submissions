class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        max_l = 0
        u_set = set()

        while r < len(s):
            while s[r] in u_set: # this moves l to the idx of a duplicate + 1
                u_set.remove(s[l]) 
                l += 1
            u_set.add(s[r])
            r += 1
            max_l = max(len(u_set), max_l)
        return max_l
            

    def lengthOfLongestSubstring2(self, s: str) -> int:
        '''
        while moving right ptr, check if the new char is in the set, is not, add if so, move the left cursor to the next letter.
        compuete the max.
        '''
        l = r = 0
        max_l = 0
        unique_set = set()
        while r < len(s):
            print("l", l, "r", r, "s[l]", s[l], "s[r]", s[r])
            if s[r] in unique_set:
                while s[l] != s[r]:
                    unique_set.remove(s[l])
                    l +=1
                l += 1
            else:
                unique_set.add(s[r])
                max_l = max(len(unique_set), max_l)
            print(unique_set, "\n")
            r += 1
        return max_l
