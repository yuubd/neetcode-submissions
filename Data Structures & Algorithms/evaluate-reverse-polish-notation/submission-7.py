class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        for each number, put them in a stack
        # nah it says the RPN is valid. For each operator, check there are at least two numbers
        For each operator, pop two numbers => compute => push back on the stack
        '''
        st = []

        for t in tokens:
            if t.lstrip("+-").isdigit():
                st.append(t)
                print(st)
            else:
                n1 = st.pop()
                n2 = st.pop()
                print("n1", n1, "n2", n2, "opr", t)
                res = self.compute(int(n1), int(n2), t)
                st.append(str(res))

        return int(st.pop())

    def compute(self, n1, n2, opr) -> int:
        match opr:
            case "+":
                return n2 + n1
            case "-":
                return n2 - n1
            case "*":
                return n2 * n1
            case "/":
                return int(n2 / n1)