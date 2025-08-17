# Microsoft, Amazon, paytm, factset, citrix
# DP on string
# LCS = longest common sub-sequence

# Top-Down(Recursion+Memoization)
# Tc = O(2^m * 2^n) => O(2^m+n) after memoization O((m+1)*(n+1)) => O(m*n)
# Sc = O(m*n)
class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.t = [[-1] * 1001 for _ in range(1001)]

    def solve(self, s1, s2, i, j):
        if i >= self.m or j >= self.n:
            return 0
        if self.t[i][j] != -1:
            return self.t[i][j]
        if s1[i] == s2[j]:
            self.t[i][j] = 1 + self.solve(s1, s2, i + 1, j + 1)
        else:
            self.t[i][j] = max(self.solve(s1, s2, i, j + 1), self.solve(s1, s2, i + 1, j))
        return self.t[i][j]

    def longestCommonSubsequence(self, s1, s2):
        self.m = len(s1)
        self.n = len(s2)
        return self.solve(s1, s2, 0, 0)
    
