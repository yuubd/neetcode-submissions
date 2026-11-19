class MinStack:
    '''
    need to maintain two stacks 
    one for real stack
    one for keeping the min

    when keeping the min stack, we only need to keep the low indexed min value.
    in case of [0 2 1, the minstack = [0 => only keep 0 cuz it is the min for all 0 2 1
    [0 2 1 -1 => then minstack = [0 -1 so push only when the val is smaller ignore all greater valiues
    '''

    def __init__(self):
        self.st = []
        self.min_st = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if len(self.min_st) == 0:
            self.min_st.append(val)
        elif val <= self.min_st[len(self.min_st)-1]:
            self.min_st.append(val)

    def pop(self) -> None:
        if self.st.pop() == self.min_st[len(self.min_st)-1]:
            self.min_st.pop()

    def top(self) -> int:
        return self.st[len(self.st)-1]

    def getMin(self) -> int:
            return self.min_st[len(self.min_st)-1]
