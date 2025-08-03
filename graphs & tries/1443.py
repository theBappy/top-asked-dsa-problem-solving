# Microsoft
# DFS approach
# Tc = O(V+E)
# Sc = O(V+E) [adjacency list]
from collections import defaultdict

class Solution:
    def dfs(self, adj, curr, parent, hasApple):
        time = 0
        for child in adj[curr]:
            if child == parent:
                continue
            time_from_child = self.dfs(adj, child, curr, hasApple)
            if time_from_child > 0 or hasApple[child]:
                time += 2 + time_from_child
        return time

    def minTime(self, n, edges, hasApple):
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return self.dfs(adj, 0, -1, hasApple)
