# Google, Amazon, Microsoft, Meta, Apple
# DFS
# Directed Graph
# If cycle return False else True
# Tc = O(V+E)
# Sc = O(V+E)
from collections import defaultdict
class Solution:
    def isCycleDFS(self, adj, u, visited, inRecursion):
        visited[u] = True
        inRecursion[u] = True
        for v in adj[u]:
            if not visited[v] and self.isCycleDFS(adj, v, visited, inRecursion):
                return True
            elif inRecursion[v]:
                return True
        inRecursion[u] = False
        return False

    def canFinish(self, numCourses, prerequisites):
        adj = defaultdict(list)
        visited = [False] * numCourses
        inRecursion = [False] * numCourses
        for a, b in prerequisites:
            adj[b].append(a)
        for i in range(numCourses):
            if not visited[i] and self.isCycleDFS(adj, i, visited, inRecursion):
                return False
        return True

