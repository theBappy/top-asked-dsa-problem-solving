# Microsoft
# Tc = O(V+E)

from collections import defaultdict
class Solution:
    def DFS(
        self, adj: dict[int, List[int]], curr: int, parent: int, hasApple: List[bool]
    ) -> int:
        time = 0
        for child in adj[curr]:
            if child == parent:
                continue
            time_from_child = self.DFS(adj, child, curr, hasApple)
            if time_from_child > 0 or hasApple[child]:
                time += time_from_child + 2
        return time

    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return self.DFS(adj, 0, -1, hasApple)
