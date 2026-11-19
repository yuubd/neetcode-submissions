class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        brackets = []

        def backtrack(openP, closeP):
            if openP is n and closeP is n:
                res.append("".join(brackets))
                return
            
            if openP < n: # add open ( always first
                brackets.append("(")
                backtrack(openP + 1, closeP)
                brackets.pop() # remove the ( and try another path
            
            # see if appending ) makes sense
            if closeP < openP:
                brackets.append(")")
                backtrack(openP, closeP + 1)
                brackets.pop()

            return
        
        backtrack(0, 0)
        return res