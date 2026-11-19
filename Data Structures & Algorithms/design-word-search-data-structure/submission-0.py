class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isWord = True

    def search(self, word: str) -> bool:
        def dfs(node, remaining_word):
            curr = node
            for i, char in enumerate(remaining_word):
                
                # encountered the wildcard, look all chlidren nodes with the remaining word
                if char == ".":
                    for child in curr.children.values():
                        if dfs(child, remaining_word[i+1:]):
                            return True
                    # tried all children but not found 
                    return False 
                        
                # normal path 
                if char not in curr.children:
                    return False
                curr = curr.children[char]
            return curr.isWord

        return dfs(self.root, word)
