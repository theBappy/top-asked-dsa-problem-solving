

# Expansion from center
# Tc = O(n^2)
# Sc = O(1)
class Solution:
    def isPal(self, string, left, right):
        while left > 0 and right < len(string) and string[left-1] == string[right+1]:
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
        self.t = [[-1] * 1001 for _ in range]
    def solve(self, s, i, j):
        if i >= j:
            return True
        if self.t[i][j] != -1:
            return self.t[i][j]
        if s[i] == s[j]:
            self.t[i][j] = self.solve(s, i+1, j-1)
            return self.t[i][j]
        self.t[i][j] == False
        return True
    def longestPalindrome(self, s:str) -> str:
        n = len(s)
        maxLen = float('-inf')
        sp = 0
        for i in range(n):
            for j in range(i, n):
                if self.solve(s, i, j):
                    if j - i + 1 > maxLen:
                        maxLen = j - i + 1
                        sp = i
        return s[sp:sp+maxLen]