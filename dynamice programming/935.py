# Google, Meta, Microsoft, DropBox
# Knight Dialer
# Without memo, Tc = 3^n
# But with memo, Tc = O(n*k) [k = 0...9=> 10 so constant for that Tc = O(n); space is also same]

# Recur + Memo
class Solution:
    def __init__(self):
        self.M = 10**9 + 7
        self.adj = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [3, 9, 0],
            [],
            [1, 7, 0],
            [2, 6],
            [1, 3],
            [2, 4]
        ]
        self.t = [[-1] * 10 for _ in range(5001)]

    def solve(self, n, cell):
        if n == 0:
            return 1
        if self.t[n][cell] != -1:
            return self.t[n][cell]
        ans = 0
        for next_cell in self.adj[cell]:
            ans = (ans + self.solve(n-1, next_cell)) % self.M
        self.t[n][cell] = ans
        return ans

    def knightDialer(self, n):
        result = 0
        for cell in range(10):
            result = (result + self.solve(n-1, cell)) % self.M


