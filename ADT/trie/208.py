class Trie:
    class TrieNode:
        def __init__(self):
            self.children = [None] * 26
            self.isEndOfWord = False

    def __init__(self):
        self.root = self.TrieNode()
        

    def insert(self, word: str) -> None:
        crawler = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if crawler.children[index] is None:
                crawler.children[index] = self.TrieNode()
            crawler = crawler.children[index]
        crawler.isEndOfWord = True
        

    def search(self, word: str) -> bool:
        crawler = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if crawler.children[index] is None:
                return False
            crawler = crawler.children[index]
        return crawler is not None and crawler.isEndOfWord
        

    def startsWith(self, prefix: str) -> bool:
        crawler = self.root

        for ch in prefix:
            index = ord(ch) - ord('a')
            if crawler.children[index] is None:
                return False
            crawler = crawler.children[index]

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)