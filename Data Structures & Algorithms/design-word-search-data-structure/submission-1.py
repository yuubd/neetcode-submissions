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
        def dfs_search(node, word_idx):
            curr = node
            for i in range(word_idx, len(word)):
                char = word[i]
                # encountered the wildcard, look all chlidren nodes with the remaining word
                if char == ".":
                    for child in curr.children.values():
                        if dfs_search(child, i+1):
                            return True
                    # tried all children but not found 
                    return False 
                        
                # normal path 
                if char not in curr.children:
                    return False
                curr = curr.children[char]
            return curr.isWord

        return dfs_search(self.root, 0)


    def dfs_search_word(node, remaining_word):
        curr = node
        for i, char in enumerate(remaining_word):
            
            # encountered the wildcard, look all chlidren nodes with the remaining word
            if char == ".":
                for child in curr.children.values():
                    if dfs_search_word(child, remaining_word[i+1:]):
                        return True
                # tried all children but not found 
                return False 
                    
            # normal path 
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.isWord
