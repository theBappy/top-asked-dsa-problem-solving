class Solution(object):
    def __init__(self):
        self.parent = []
        self.rank = []

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
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

    def kruskal(self, edges):
        total_cost = 0
        for u, v, wt in edges:
            if self.find(u) != self.find(v):
                self.union(u, v)
                total_cost += wt
        return total_cost

    def minCostConnectPoints(self, points):
        V = len(points)
        self.parent = [i for i in range(V)]
        self.rank = [0] * V

        edges = []

        for i in range(V):
            for j in range(i+1, V):
                x1, y1 = points[i]
                x2, y2 = points[j]

                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((i, j, dist))

        edges.sort(key=lambda x: x[2])
        return self.kruskal(edges)
 