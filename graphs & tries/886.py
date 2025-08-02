# Microsoft, FlipKart, Samsung
# Tc = O(V + E)
# Sc = O(V + E)
from collections import deque

class Solution:
    def bfsCheckBipartite(self, adj: dict[int, list[int]], start_node: int, color: list[int]) -> bool:
        q = deque()
        q.append(start_node)
        color[start_node] = 0

        while q:
            u = q.popleft()
            for v in adj.get(u, []):
                if color[v] == color[u]:
                    return False
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    q.append(v)
        return True

    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        adj = {i: [] for i in range(1, n + 1)}
        for u, v in dislikes:
            adj[u].append(v)
            adj[v].append(u)

        color = [-1] * (n + 1)
        
        for i in range(1, n + 1):
            if color[i] == -1:
                if not self.bfsCheckBipartite(adj, i, color):
                    return False
        
        return True