class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        '''
        10:47
        Create a Trie with the words
        state
            Trie = with char, isWord, children = {}
            for each cell, O(n^2)
                search for words if the first chat is a match O(n^2 )
                if found a word, add it to output
                dont end there but try all with dfs
        '''


        root = Trie("ROOT")
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = Trie(char, False, {})
                node = node.children[char]
            print(node.char)
            node.isWord = True

        output = set()
        visited = set()
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfsTrie(r, c, node, word):
            if (r, c) in visited:
                return
            visited.add((r, c))

            word += node.char
            # print(word, node.isWord)
            if node.isWord:
                output.add(word)

            for dr, dc in dirs:
                nr, nc = dr+r, dc+c

                if not (0 <= nr <= R-1 and 0 <= nc <= C-1):
                    continue
                char = board[nr][nc]
                if char not in node.children:
                    continue 
                dfsTrie(nr, nc, node.children[char], word)
            visited.remove((r,c))
        
        R, C = len(board), len(board[0])
        for r in range(R):
            for c in range(C):
                char = board[r][c]
                if char not in root.children:
                    continue
                dfsTrie(r, c, root.children[char], "")

        return list(output)

                

        # node = None
        # st = [root]
        # while st:
        #     node = st.pop()
        #     print(node.char)
        #     for _, child in node.children.items():
        #         st.append(child)
        






class Trie:
    def __init__(self, char, isWord = False, children = None):
        self.char = char
        self.isWord = isWord
        self.children = children if children != None else {}