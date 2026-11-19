class Solution:
    
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        l = r = 0
        maxSubLen = 0
        maxFreqSeenSoFar = 0
        while r < len(s):
            freq[s[r]] += 1
            maxFreqSeenSoFar = max(maxFreqSeenSoFar, freq[s[r]])
            # windowSize = r - l + 1
            while (r - l + 1) - maxFreqSeenSoFar > k:
                freq[s[l]] -= 1
                l += 1

            maxSubLen = max(maxSubLen, (r - l + 1))
            r += 1
        return maxSubLen




    def characterReplacement2(self, s: str, k: int) -> int:
        '''
        In an any window, window len - the most frequent char is the number of chars we need to substitude to make the whole window same char
        So while increasing the window from the left, update a frequency map.
        If len(window - most frequent char) >= k, keep moving to right
        else, move left
        record the len of window all the time

        return the max len

        do it until r < len
        '''
        max_len = 0

        l = r = 0
        freq_m = defaultdict(int)
        curr_most_freq_char = s[l]

        while r < len(s):
            freq_m[s[r]] += 1
            # print("l", l, "r", r, "curr_most_freq_char", curr_most_freq_char, "max_len", max_len, "freq_m", freq_m)
            
            if freq_m[s[r]] > freq_m[curr_most_freq_char]:
                curr_most_freq_char = s[r]
            win_len = r - l + 1
            
            if win_len - freq_m[curr_most_freq_char] <= k: # green expand to right
                max_len = max(max_len, win_len)
            else: 
                freq_m[s[l]] -= 1
                l += 1
            r += 1
        
        return max_len
            