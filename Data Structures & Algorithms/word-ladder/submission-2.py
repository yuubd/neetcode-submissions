class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        patternToWords = defaultdict(list)
        endWordPresent = False
        for w in wordList + [beginWord]:
            for i in range(len(w)):
                pattern = w[:i] + "*" + w[i+1:]
                patternToWords[pattern].append(w)
            if w == endWord:
                endWordPresent = True
        if not endWordPresent:
            return 0
        print(patternToWords)
        visited = set()
        q = deque([[beginWord, 1]])
        currWord = ""
        res = 1
        while len(q) > 0:
            currWord, length = q.popleft()
            if currWord in visited:
                continue
            print(currWord)
            if currWord == endWord:
                return length
            visited.add(currWord)
            for i in range(len(currWord)):
                pattern = currWord[:i] + "*" + currWord[i+1:]
                nextWords = patternToWords[pattern]
                for nextWord in nextWords:
                    q.append([nextWord, length+1])
        return 0
        

        


