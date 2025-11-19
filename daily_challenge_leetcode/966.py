# Tc = O(N) #N = total length of all the input strings and queries
# Sc = O(N)

class Solution:
    def __init__(self):
        self.exactWords = set()          # stores original words
        self.caseMap = {}                # lowercase : original word
        self.vowelMap = {}               # masked vowels : original word

    def toLower(self, s: str) -> str:
        return s.lower()

    def maskVowels(self, s: str) -> str:
        return ''.join('*' if c in 'aeiou' else c for c in s)

    def checkForMatch(self, query: str) -> str:
        # Exact match
        if query in self.exactWords:
            return query

        # Case error match
        lowerQuery = self.toLower(query)
        if lowerQuery in self.caseMap:
            return self.caseMap[lowerQuery]

        # Vowel error match
        maskedQuery = self.maskVowels(lowerQuery)
        if maskedQuery in self.vowelMap:
            return self.vowelMap[maskedQuery]

        # 4. No match
        return ""

    def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
        self.exactWords.clear()
        self.caseMap.clear()
        self.vowelMap.clear()

        for word in wordlist:
            self.exactWords.add(word)

            lowerWord = self.toLower(word)
            if lowerWord not in self.caseMap:  # Add only 1st occurrence
                self.caseMap[lowerWord] = word

            maskedWord = self.maskVowels(lowerWord)
            if maskedWord not in self.vowelMap:  # Add only 1st occurrence
                self.vowelMap[maskedWord] = word

        result = []
        for query in queries:
            result.append(self.checkForMatch(query))
        return result





from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # Lowercase map for case-insensitive
        capital = {w.lower(): w for w in wordlist[::-1]}
        # Vowel-masked map for vowel-insensitive
        vowel = {
            ''.join([ch if ch not in "aeiou" else '*' for ch in w.lower()]): w
            for w in wordlist[::-1]
        }
        wordset = set(wordlist)

        res = []
        for q in queries:
            if q in wordset:
                res.append(q)
            elif q.lower() in capital:
                res.append(capital[q.lower()])
            else:
                masked = ''.join([ch if ch not in "aeiou" else '*' for ch in q.lower()])
                res.append(vowel.get(masked, ""))
        return res

    
    




    