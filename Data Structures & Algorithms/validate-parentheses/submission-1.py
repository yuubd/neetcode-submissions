class Solution:
    def isValid(self, s: str) -> bool:
        st = [] # stack
        for b in s:
            if b == "{" or b == "(" or b == "[":
                st.append(b)
            else:
                if len(st) == 0:
                    return False
                open_b = st.pop()
                if open_b == "{" and b == "}":
                    continue
                if open_b == "(" and b == ")":
                    continue
                if open_b == "[" and b == "]":
                    continue
                return False
        
        return len(st) == 0