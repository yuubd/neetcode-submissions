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
            # print(s[i].isalnum(), s[j].isalnum())
            # while i < len(clean_s)-1 and not clean_s[i].isalnum():
            #     i += 1
            # while j > 0 and not clean_s[j].isalnum():
            #     j -= 1
            # print(clean_s[i].lower(), clean_s[j].lower())
            if clean_s[i].lower() != clean_s[j].lower():
                return False
            i += 1
            j -= 1
        return True
        