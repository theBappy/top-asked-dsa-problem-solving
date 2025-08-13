# Google, Samsung
# Tc = O(N.L) [number of word * word avg length]
# Sc = O(N.L)

class TrieNode:
    def __init__(self):
        self.countPrefix = 0
        self.children = [None] * 26

class Solution:
    def getTrieNode(self):
        newNode = TrieNode()
        newNode.countPrefix = 0
        return newNode

    def insert(self, word, root):
        crawl = root
        for ch in word:
            idx = ord(ch) - ord('a')
            if crawl.children[idx] is None:
                crawl.children[idx] = self.getTrieNode()
            crawl.children[idx].countPrefix += 1
            crawl = crawl.children[idx]

    def getScore(self, word, root):
        crawl = root
        score = 0
        for ch in word:
            idx = ord(ch) - ord('a')
            score += crawl.children[idx].countPrefix
            crawl = crawl.children[idx]
        return score

    def sumPrefixScores(self, words):
        n = len(words)
        root = self.getTrieNode()
        for word in words:
            self.insert(word, root)
        result = [0] * n
        for i in range(n):
            result[i] = self.getScore(words[i], root)
        return result