class StringIterator:

    def __init__(self, compressedString: str):
        self.q = deque()

        i = 0
        curIdx = 0
        while i < len(compressedString):
            char = compressedString[i]
            i += 1 
            count = []
            while i < len(compressedString) and compressedString[i].isdigit():
                count.append(compressedString[i])
                i += 1
            # print(char)
            # print(count)
            count = int("".join(count))
            self.q.append([count, char])
            # curIdx += count
        print(self.q)
            


    def next(self) -> str:
        count, char = self.q[0]
        count -= 1
        if count == 0:
            self.q.popleft()
        else:
            self.q[0][0] = count

        return char
        
    def hasNext(self) -> bool:
        return len(self.q) > 0
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
