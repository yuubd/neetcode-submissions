class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        '''
        node is letter, edge is directed eeg z -> o
        output = the letters in directed order => topology sort

        we need adj and indeg maps
        for prev and curr words in words:
            for each i th letters in two words:
                if letters are diff and currL not in adj[prevL]:
                    adj[prevL].add(currL)
                    indeg[currL] += 1
                    break
                else:
                    if len prev > curr and i == len curr -1:
                        return ""
        
        output = []
        with a deque where init entry is letter with 0 indeg # if cycle, those nodes will not be added to queue
        while q:
            curr l popped 
            output append the curr l
            for adj in currl:
                indeg[adj] -= 1
                append to q if indeg[adj] == 0
            
        return output.join('') if len(output) == len(indeg) len is > 0 else "" # if 
        '''

        indegMap = {l:0 for w in words for l in w} # all letters. letter: indeg #
        adjMap = {l: set() for l in indegMap.keys()} # letter: adj letters
        
        for prev, curr in zip(words, words[1:]):
            print(prev, curr)
            for prevL, currL in zip(prev, curr):
                if prevL != currL:
                    if currL not in adjMap[prevL]:
                        adjMap[prevL].add(currL)
                        indegMap[currL] += 1
                    break
            else:
                if len(prev) > len(curr):
                    return ""
            prev = curr
        
        q = deque() # letter with 0 indeg
        for l, indeg in indegMap.items():
            if indeg == 0:
                q.append(l)

        output = []
        while q:
            letter = q.popleft()
            output.append(letter)
            for adjLetter in adjMap[letter]:
                indegMap[adjLetter] -= 1
                if indegMap[adjLetter] == 0:
                    q.append(adjLetter)

        return ''.join(output) if len(output) == len(adjMap) else ""











