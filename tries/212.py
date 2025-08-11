# Google, Microsoft, Yahoo, Apple
# Tc = O(m.k + r.c.4^k)
# Sc = O(m.k)

class TrieNode:
    def __init__(self):
        self.end_of_word = False
        self.children = {}
        self.word = ""

class Solution:
    def __init__(self):
        self.result = []
        self.r = 0
        self.c = 0
        self.directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def insert(self, root, word):
        pCrawl = root
        for ch in word:
            if ch not in pCrawl.children:
                pCrawl.children[ch] = TrieNode()
            pCrawl = pCrawl.children[ch]
        pCrawl.end_of_word = True
        pCrawl.word = word

    def DFS(self, board, i, j, root):
        if i < 0 or i >= self.r or j < 0 or j >= self.c or board[i][j] == '$' or board[i][j] not in root.children:
            return
        
        root = root.children[board[i][j]]
        if root.end_of_word:
            self.result.append(root.word)
            root.end_of_word = False  # avoid duplicates
        
        temp = board[i][j]
        board[i][j] = '$'  # mark as visited
        
        for direction in self.directions:
            new_i, new_j = i + direction[0], j + direction[1]
            self.DFS(board, new_i, new_j, root)
        
        board[i][j] = temp  # restore the original character

    def findWords(self, board, words):
        self.r = len(board)
        self.c = len(board[0]) if self.r > 0 else 0

        root = TrieNode()
        for word in words:
            self.insert(root, word)

        for i in range(self.r):
            for j in range(self.c):
                if board[i][j] in root.children:
                    self.DFS(board, i, j, root)

        return self.result
