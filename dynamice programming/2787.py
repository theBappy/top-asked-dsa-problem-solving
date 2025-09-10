# Google, Apple

# Knapsack

class Solution(object):
    def __init__(self):
        self.M = int(1e9 + 7)
        self.t = [[-1] * 301 for _ in range(301)]

    def solve(self, n, num, x):
        if n == 0:
            return 1
        if n < 0:
            return 0
        currPowerVal = num ** x
        if currPowerVal > n:
            return 0
        if self.t[n][num] != -1:
            return self.t[n][num]
        take = self.solve(n - currPowerVal, num + 1, x)
        skip = self.solve(n, num + 1, x)
        self.t[n][num] = (take + skip) % self.M
        return self.t[n][num]

    def numberOfWays(self, n, x):
        self.t = [[-1] * 301 for _ in range(301)]
        return self.solve(n, 1, x)