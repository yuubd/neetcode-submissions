class MyQueue:

    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, x: int) -> None:
        if self.outStack:
            self.inStack = self.outStack[::-1]
            self.outStack = []
        self.inStack.append(x)

    def pop(self) -> int:
        if self.inStack:
            self.outStack = self.inStack[::-1]
            self.inStack = []
        return self.outStack.pop()

    def peek(self) -> int:
        if self.inStack:
            self.outStack = self.inStack[::-1]
            self.inStack = []
        return self.outStack[-1]

    def empty(self) -> bool:
        print(self.outStack, self.inStack)
        if len(self.outStack) == 0 and len(self.inStack) == 0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()