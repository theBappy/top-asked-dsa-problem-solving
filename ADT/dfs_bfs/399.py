# Meta, Amazon, Google
# Tc = O(n * (V + E)) [queries * V + E]

from collections import defaultdict


class Solution:
    def dfs(self, adj, src, dst, visited, product, ans):
        if src in visited:
            return
        visited.add(src)
        if src == dst:
            ans[0] = product
            return
        for v, val in adj[src]:
            self.dfs(adj, v, dst, visited, product * val, ans)

    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        adj = defaultdict(list)
        for (u, v), val in zip(equations, values):
            adj[u].append((v, val))
            adj[v].append((u, 1.0 / val))
        result = []
        for src, dst in queries:
            ans = [-1.0]
            product = 1.0
            if src in adj:
                visited = set()
                self.dfs(adj, src, dst, visited, product, ans)
            result.append(ans[0])
        return result
