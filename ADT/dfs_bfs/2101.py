# Google

# DFS
from collections import defaultdict


class Solution:
    def DFS(self, u, visited, adj):
        visited.add(u)
        for v in adj[u]:
            if v not in visited:
                self.DFS(v, visited, adj)

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        adj = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]

                distance = (x2 - x1) ** 2 + (y2 - y1) ** 2
                if r1 * r1 >= distance:
                    adj[i].append(j)

        result = 0
        visited = set()
        for i in range(n):
            self.DFS(i, visited, adj)
            count = len(visited)
            result = max(result, count)
            visited.clear()
        return result


# BFS
from collections import defaultdict, deque


class Solution:
    def BFS(self, u, adj):
        visited = set()
        que = deque()
        que.append(u)
        visited.add(u)
        while que:
            temp = que.popleft()
            for v in adj.get(temp, []):
                if v not in visited:
                    que.append(v)
                    visited.add(v)
        return len(visited)

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        adj = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]

                distance = (x2 - x1) ** 2 + (y2 - y1) ** 2
                if r1 * r1 >= distance:
                    adj[i].append(j)

        result = 0
        for i in range(n):
            count = self.BFS(i, adj)
            result = max(result, count)
        return result
