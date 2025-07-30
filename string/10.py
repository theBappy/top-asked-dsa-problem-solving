class Solution:
    def __init__(self):
        self.t = [[-1] * 21 for _ in range(21)]

    def solve(self, i, j, s, p):
        if j == len(p):
            return i == len(s)
        if self.t[i][j] != -1:
            return self.t[i][j]
        first_char_matched = False
        if i < len(s) and (p[j] == s[i] or p[j] == '.'):
            first_char_matched = True
        if j + 1 < len(p) and p[j + 1] == '*':
            not_take = self.solve(i, j + 2, s, p)
            take = first_char_matched and self.solve(i + 1, j, s, p)
            self.t[i][j] = not_take or take
            return self.t[i][j]
        self.t[i][j] = first_char_matched and self.solve(i + 1, j + 1, s, p)
        return self.t[i][j]

    def isMatch(self, s, p):
        self.t = [[-1] * 21 for _ in range(21)]
        return self.solve(0, 0, s, p)