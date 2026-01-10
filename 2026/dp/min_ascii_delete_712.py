class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.t = []

    def solve(self, s1, s2, i, j):
        if i >= self.m and j >= self.n:
            return 0

        if self.t[i][j] != -1:
            return self.t[i][j]

        if i >= self.m:
            self.t[i][j] = ord(s2[j]) + self.solve(s1, s2, i, j + 1)
            return self.t[i][j]
        elif j >= self.n:
            self.t[i][j] = ord(s1[i]) + self.solve(s1, s2, i + 1, j)
            return self.t[i][j]

        if s1[i] == s2[j]:
            self.t[i][j] = self.solve(s1, s2, i + 1, j + 1)
            return self.t[i][j]

        take_s1_i = ord(s1[i]) + self.solve(s1, s2, i + 1, j)
        take_s2_j = ord(s2[j]) + self.solve(s1, s2, i, j + 1)

        self.t[i][j] = min(take_s1_i, take_s2_j)
        return self.t[i][j]

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        self.m = len(s1)
        self.n = len(s2)
        self.t = [[-1] * (self.n + 1) for _ in range(self.m + 1)]
        return self.solve(s1, s2, 0, 0)
