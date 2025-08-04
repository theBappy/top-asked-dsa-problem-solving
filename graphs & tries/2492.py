# GOOGLE
# Minimum score(distance) of path between two cities
# Undirected Graph
# 1 to n (1->4)
# DFS Traversal
# Tc = O(V + E)
# Sc = O(V + E)

from collections import defaultdict
import sys

class Solution:
    def dfs(self, u, adj, visited, result):
        visited.add(u)  # set to track visited nodes
        for v, d in adj[u]:
            result[0] = min(result[0], d)
            if v not in visited:
                self.dfs(v, adj, visited, result)

    def minScore(self, n, roads):
        adj = defaultdict(list)
        for u, v, d in roads:
            adj[u].append((v, d))
            adj[v].append((u, d))
        
        visited = set()  # set for visited nodes
        result = [sys.maxsize]  # list to allow modification in dfs
        self.dfs(1, adj, visited, result)
        return result[0]

