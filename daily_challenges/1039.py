import sys
class Solution(object):
    def __init__(self):
        self.t = []
    def solve(self, values, i, j):
        if j - i + 1 < 3:
            return 0
        if self.t[i][j] != -1:
            return self.t[i][j]
        result = sys.maxsize
        for k in range(i+1, j):
            wt = (values[i] * values[j] * values[k]) + self.solve(values, i, k) + self.solve(values, k, j)
            result = min(result, wt)
        self.t[i][j] = result
        return result
    
    def minScoreTriangulation(self, values):
        n = len(values)
        self.t = [[-1] * n for _ in range(n)]
        return self.solve(values, 0, n-1)