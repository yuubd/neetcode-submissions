class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        '''
        10:05
        BF: 
        for each word,
            do another scan on words from i+1 to end
                check the next word to check the prefix and suffix
                if so, += 1
        O(n^2)
        '''

        # count = 0
        # for i, word in enumerate(words): 
        #     for nextWord in words[i + 1:]:
        #         if nextWord.startswith(word) and nextWord.endswith(word):
        #             count += 1
        # return count
        root = Trie()
        count = 0
        for word in words:
            node = root
            for i, char in enumerate(word):
                postChar = word[-1-i]
                key = (char, postChar)
                if not key in node.children:
                    node.children[key] = Trie()
                count += node.children[key].count
                node = node.children[key]
            node.count += 1
        # print_trie(root)
        return count

from collections import deque
def print_trie(root):
    queue = deque([root])

    while queue:
        level = []
        next_queue = deque()

        while queue:
            node = queue.popleft()

            # Print the keys/edges leaving this node
            level.append(list(node.children.keys()))

            for child in node.children.values():
                next_queue.append(child)

        print(level)
        queue = next_queue





class Trie:
    def __init__(self, count = 0, children = None):
        self.count = count
        self.children = {}
        