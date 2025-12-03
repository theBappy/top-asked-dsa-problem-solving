// Using DFS
from collections import defaultdict


class Solution:
    def isSimilar(self, s1: str, s2: str) -> bool:
        diff = 0
        for a, b in zip(s1, s2):
            if a != b:
                diff += 1
        return diff == 2 or diff == 0

    def DFS(self, u: int, adj: dict, visited: list):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                self.DFS(v, adj, visited)

    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        adj = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                if self.isSimilar(strs[i], strs[j]):
                    adj[i].append(j)
                    adj[j].append(i)
        visited = [False] * n
        count = 0
        for i in range(n):
            if not visited[i]:
                self.DFS(i, adj, visited)
                count += 1
        return count
