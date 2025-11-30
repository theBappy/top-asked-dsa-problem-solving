from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        queue = deque([(beginWord, 1)])  # store (word, steps)

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps

            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    next_word = word[:i] + ch + word[i+1:]

                    if next_word in wordSet:
                        wordSet.remove(next_word)  
                        queue.append((next_word, steps + 1))

        return 0
