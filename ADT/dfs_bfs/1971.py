# Microsoft, Amazon, Adobe

# Using DFS
# Tc = O(m + n)
from collections import defaultdict


class Solution:
    def check(self, mp, node, destination, visited):
        if node == destination:
            return True
        if visited[node]:
            return False
        visited[node] = True
        for it in mp[node]:
            if self.check(mp, it, destination, visited):
                return True
        return False

    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        if source == destination:
            return True
        mp = defaultdict(list)
        for u, v in edges:
            mp[u].append(v)
            mp[v].append(u)
        visited = [False] * n
        return self.check(mp, source, destination, visited)


# Using BFS
from collections import defaultdict, deque


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        mp = defaultdict(list)
        for u, v in edges:
            mp[u].append(v)
            mp[v].append(u)
        visited = [False] * n
        que = deque([source])
        visited[source] = True
        while que:
            node = que.popleft()
            if node == destination:
                return True
            for neighbor in mp[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    que.append(neighbor)
        return False
