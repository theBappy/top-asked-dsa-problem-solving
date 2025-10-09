# Tc = O(n^2)
# Sc = O(n^2)
class Solution:
    def __init__(self):
        self.t = None

    def solve(self, s, l, r):
        if l >= r:
            return True

        if self.t[l][r] is not None:
            return self.t[l][r]

        if s[l] == s[r]:
            self.t[l][r] = self.solve(s, l + 1, r - 1)
            return self.t[l][r]

        self.t[l][r] = False
        return False

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        self.t = [[None] * n for _ in range(n)]

        maxlen = float('-inf')
        startingIndex = 0

        for i in range(n):
            for j in range(i, n):
                if self.solve(s, i, j):
                    if j - i + 1 > maxlen:
                        startingIndex = i
                        maxlen = j - i + 1

        return s[startingIndex:startingIndex + maxlen]