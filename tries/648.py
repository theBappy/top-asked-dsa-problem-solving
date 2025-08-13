# Facebook, Instagram
# Tc = O(n * l)
# Sc = O(n * l)

class Solution:
    class TrieNode:
        def __init__(self):
            self.children = [None] * 26
            self.isEnd = False

    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return self.TrieNode()

    def insert(self, word):
        crawler = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if crawler.children[idx] is None:
                crawler.children[idx] = self.getNode()
            crawler = crawler.children[idx]
        crawler.isEnd = True

    def search(self, word):
        crawler = self.root
        for i, char in enumerate(word):
            idx = ord(char) - ord('a')
            if crawler.children[idx] is None:
                return word
            crawler = crawler.children[idx]
            if crawler.isEnd:
                return word[:i + 1]
        return word

    def replaceWords(self, dictionary, sentence):
        for word in dictionary:
            self.insert(word)
        words = sentence.split(' ')
        result = []
        for word in words:
            result.append(self.search(word))
        return ' '.join(result)
