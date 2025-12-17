class TrieNode:
    def __init__(self):
        # Each node has 26 children (for 'a' to 'z')
        # Space: O(26) → O(1)
        self.children = [None] * 26
        self.isEndOfWord = False


class Solution:
    def __init__(self):
        # Root of the Trie
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Start from root
        crawler = self.root

        # Loop through each character of the word
        # Time: O(len(word))
        for ch in word:
            index = ord(ch) - ord('a')  # Convert char to index (0–25)

            # If node does not exist, create it
            # Node creation: O(1)
            if crawler.children[index] is None:
                crawler.children[index] = TrieNode()

            # Move to next node
            crawler = crawler.children[index]

        # Mark end of word
        crawler.isEndOfWord = True

    def search(self, word: str) -> str:
        # Start from root
        crawler = self.root

        # Traverse characters of word
        # Time: O(len(word))
        for i, ch in enumerate(word):
            index = ord(ch) - ord('a')

            # If path breaks, no prefix exists
            if crawler.children[index] is None:
                return word  # O(1)

            crawler = crawler.children[index]

            # If a root word ends here, return prefix
            if crawler.isEndOfWord:
                return word[:i + 1]  # O(i)

        # If no root word matched
        return word

    def replaceWords(self, dictionary, sentence: str) -> str:
        # Insert all dictionary words into Trie
        # Time: O(D * L)
        for word in dictionary:
            self.insert(word)

        result = []

        # Split sentence into words
        # Time: O(S)
        for word in sentence.split():
            # Search smallest prefix for each word
            # Time per word: O(M)
            result.append(self.search(word))

        # Join result words into sentence
        # Time: O(S)
        return " ".join(result)
