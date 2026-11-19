class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        clean_s = ""
        for char in s:
            if not char.isalnum() or char == " ":
                continue
            clean_s += char
        # print("clean_s", clean_s)

        i = 0
        j = len(clean_s)-1
        while i <= j:
            if clean_s[i].lower() != clean_s[j].lower():
                return False
            i += 1
            j -= 1
        return True
        