from collections import defaultdict
class Solution:
    def isBipartite(
        self, adj: dict[int, List[int]], node: int, color: List[int]
    ) -> bool:
        que = deque([node])
        color[node] = 1
        while que:
            u = que.popleft()
            for v in adj[u]:
                if color[v] == color[u]:
                    return False
                if color[v] == -1:
                    que.append(v)
                    color[v] = 1 - color[u]
        return True

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u, v in dislikes:
            adj[u].append(v)
            adj[v].append(u)
        color = [-1] * (n + 1)
        for i in range(n + 1):
            if color[i] == -1:
                if not self.isBipartite(adj, i, color):
                    return False
        return True
