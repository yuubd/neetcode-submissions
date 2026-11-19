class Solution:
    def isValid(self, s: str) -> bool:
        st = [] # stack
        bracket_map = {"}":"{", ")":"(", "]":"[" }
        for b in s:
            if b not in bracket_map:
                st.append(b)
            else:
                if len(st) > 0 and bracket_map[b] == st.pop():
                    continue
                else:
                    return False
        return len(st) == 0