# Instagram, facebook, twitter, whatsapp
# Prefix/Suffix in multiple string -> TRIE(prefix tree/suffix tree)
# Store opposite in Trie for easily match
# Where to search, these elements always store in TRIE


class TrieNode:
    def __init__(self):
        self.index = inf
        self.children = [None] * 26

class Trie:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.words = words
        for i, word in enumerate(words):
            self.insertSuffix(word, i)
    
    def change(self, i: int, j: int) -> bool: # change i to j ?
        # j should be valid
        # change if i is not valid, or if less size,
        # or if less index: REMOVED as we are inserting words from container with increasing index
        n = len(self.words)
        return (0 <= j < n) and (not (0 <= i < n) or len(self.words[j]) < len(self.words[i]))
    
    def insertSuffix(self, s: str, index: int):
        curr = self.root

        for ch in s[::-1]:
            i = ord(ch) - ord('a')
            if not curr.children[i]:
                curr.children[i] = TrieNode()
            if self.change(curr.index, index):
                curr.index = index
            curr = curr.children[i]
        
        if self.change(curr.index, index):
            curr.index = index
    
    def longestCommonSuffix(self, s: str) -> int:
        curr = self.root
        for ch in s[::-1]:
            i = ord(ch) - ord('a')
            if not curr.children[i]:
                break
            curr = curr.children[i]
        return curr.index

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = Trie(wordsContainer)
        return [trie.longestCommonSuffix(word) for word in wordsQuery]