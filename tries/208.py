class Trie:
    
    class TrieNode:
        def __init__(self):
            self.children = [None] * 26
            self.is_end_of_word = False
            
    def __init__(self):
        self.root = self.get_node()
        
    def get_node(self):
        return self.TrieNode()
    
    def insert(self, word: str) -> None:
        crawler = self.root
        
        for char in word:
            index = ord(char) - ord('a')
            if crawler.children[index] is None:
                crawler.children[index] = self.get_node()
            crawler = crawler.children[index]
        
        crawler.is_end_of_word = True
    
    def search(self, word: str) -> bool:
        crawler = self.root
        
        for char in word:
            index = ord(char) - ord('a')
            if crawler.children[index] is None:
                return False
            crawler = crawler.children[index]
        
        return crawler is not None and crawler.is_end_of_word
    
    def starts_with(self, prefix: str) -> bool:
        crawler = self.root
        
        for char in prefix:
            index = ord(char) - ord('a')
            if crawler.children[index] is None:
                return False
            crawler = crawler.children[index]
        
        return True