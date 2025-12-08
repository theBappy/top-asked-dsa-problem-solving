from collections import deque
from math import inf


class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        result = inf
        for start in range(n):
            dist = [-1] * n
            parent = [-1] * n
            q = deque()
            dist[start] = 0
            q.append(start)
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        parent[v] = u
                        q.append(v)
                    elif parent[u] != v:
                        result = min(result, dist[u] + dist[v] + 1)
        return -1 if result == inf else result
