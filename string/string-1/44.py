class Solution:
    def solve(self, i, j, s, p, dp):
        # Base cases
        if i == len(s) and j == len(p):
            return True  # both exhausted
        if j == len(p):
            return False  # pattern finished, but string not
        if i == len(s):
            # remaining pattern must all be '*'
            return all(ch == '*' for ch in p[j:])
        
        if dp[i][j] != -1:
            return dp[i][j]

        # Case 1: Direct match or '?'
        if p[j] == s[i] or p[j] == '?':
            dp[i][j] = self.solve(i + 1, j + 1, s, p, dp)
        
        # Case 2: '*'
        elif p[j] == '*':
            # '*' → match empty (move pattern) OR consume one char (move string)
            dp[i][j] = self.solve(i, j + 1, s, p, dp) or self.solve(i + 1, j, s, p, dp)
        
        # Case 3: Mismatch
        else:
            dp[i][j] = False
        
        return dp[i][j]

    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[-1] * (n + 1) for _ in range(m + 1)]
        return self.solve(0, 0, s, p, dp)
