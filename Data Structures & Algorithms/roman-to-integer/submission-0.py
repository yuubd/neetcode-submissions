class Solution:
    def romanToInt(self, s: str) -> int:
        convert = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        res = 0
        i = 0
        while i < len(s):
            curr = s[i]
            nxt = s[i+1] if i < len(s)-1 else None
            if curr == "I" and nxt in ("V", "X"):
                res += (convert[nxt] - convert[curr])
                i += 2
            elif curr == "X" and nxt in ("L", "C"):
                res += (convert[nxt] - convert[curr])
                i += 2
            elif curr == "C" and nxt in ("D", "M"):
                res += (convert[nxt] - convert[curr])
                i += 2
            else:
                res += convert[curr]
                i += 1
        return res

