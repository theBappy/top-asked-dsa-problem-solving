
# Expansion from center
# Tc = O(n^2)
# Sc = O(1)
class Solution:
    def isPal(self, string, left, right):
        while left > 0 and right < len(string) -1 and string[left-1] == string[right+1]:
            left -= 1
            right += 1
        return left, right, right - left + 1

    def longestPalindrome(self, s:str) -> str:
        max_len, left, right = 0, 0, 0
        for index in range(len(s) -1):
            # middle is a char
            # odd-length
            l1, r1, max_len1 = self.isPal(s, index, index)
            if max_len1 > max_len:
                max_len = max_len1
                left, right = l1, r1 
            # middle between two char
            # even-length
            if s[index] == s[index+1]:
                l2, r2, max_len2 = self.isPal(s, index, index+1)
                if max_len2 > max_len:
                    max_len = max_len2
                    left, right = l2, r2
        return s[left:right+1]


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