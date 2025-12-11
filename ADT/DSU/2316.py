from collections import defaultdict


class Solution:
    def __init__(self):
        self.parent = []
        self.rank = []

    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def Union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[px] < self.rank[py]:
            self.parent[px] = py
        else:
            self.parent[px] = py
            self.rank[py] += 1

    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        self.parent = list(range(n))
        self.rank = [0] * n
        for u, v in edges:
            self.Union(u, v)
        mp = defaultdict(int)
        for i in range(n):
            head = self.find(i)
            mp[head] += 1

        result = 0
        remaining_nodes = n
        for size in mp.values():
            result += size * (remaining_nodes - size)
            remaining_nodes -= size
        return result
