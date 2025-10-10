# Tc = O(m.n)
# Sc = O(m.n)
class Solution:
    def solve(self, i, j, s, p, t):
        if j == len(p):
            return i == len(s)
        if t[i][j] != -1:
            return t[i][j]
        first_char_matched = False
        if i < len(s) and (p[j] == s[i] or p[j] == '.'):
            first_char_matched = True
        if j + 1 < len(p) and p[j + 1] == '*':
            not_take = self.solve(i, j + 2, s, p, t)
            take = first_char_matched and self.solve(i + 1, j, s, p, t)
            t[i][j] = not_take or take
        else:
            t[i][j] = first_char_matched and self.solve(i + 1, j + 1, s, p, t)
        return t[i][j]
    
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        t = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        return self.solve(0, 0, s, p, t)



from functools import lru_cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def solve(i: int, j: int) -> bool:
            if j == len(p):
                return i == len(s)
            
            first_char_matched = i < len(s) and (p[j] == s[i] or p[j] == '.')
            
            if j + 1 < len(p) and p[j + 1] == '*':
                not_take = solve(i, j + 2)
                take = first_char_matched and solve(i + 1, j)
                return not_take or take
            
            return first_char_matched and solve(i + 1, j + 1)
        
        return solve(0, 0)