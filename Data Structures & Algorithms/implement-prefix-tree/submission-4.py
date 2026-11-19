class PrefixTreeNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.treeRoot = PrefixTreeNode()

    def insert(self, word: str) -> None:
        currNode = self.treeRoot
        for char in word:
            if char not in currNode.children:
                currNode.children[char] = PrefixTreeNode()
            currNode = currNode.children[char]
        currNode.isWord = True

    def search(self, word: str) -> bool:
        currNode = self.treeRoot
        for char in word:
            if char not in currNode.children:
                return False
            currNode = currNode.children[char]
        return currNode.isWord

    def startsWith(self, prefix: str) -> bool:
        currNode = self.treeRoot
        for char in prefix:
            if char not in currNode.children:
                return False
            currNode = currNode.children[char]
        return True
        
