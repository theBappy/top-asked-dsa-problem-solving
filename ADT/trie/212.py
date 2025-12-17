class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        result = []
        r, c = len(board), len(board[0])

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        # Trie node structure using dict
        class TrieNode:
            def __init__(self):
                self.endOfWord = False
                self.children = {}
                self.word = ""

        # Create root
        root = TrieNode()

        # Insert words into Trie (same logic as C++)
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.endOfWord = True
            node.word = word

        # DFS function (same logic)
        def DFS(i, j, node):
            if (
                i < 0 or i >= r or
                j < 0 or j >= c or
                board[i][j] == '$' or
                board[i][j] not in node.children
            ):
                return

            node = node.children[board[i][j]]

            if node.endOfWord:
                result.append(node.word)
                node.endOfWord = False   # avoid duplicates

            temp = board[i][j]
            board[i][j] = '$'           # mark visited

            for dx, dy in directions:
                DFS(i + dx, j + dy, node)

            board[i][j] = temp           # backtrack

        # Start DFS from each cell
        for i in range(r):
            for j in range(c):
                if board[i][j] in root.children:
                    DFS(i, j, root)

        return result
