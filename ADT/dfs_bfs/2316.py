from collections import defaultdict


class Solution:
    def dfs(self, u, adj, visited):
        visited[u] = True
        sizeOfComponent = 1
        for v in adj[u]:
            if not visited[v]:
                sizeOfComponent += self.dfs(v, adj, visited)
        return sizeOfComponent

    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        remainingNodes = n
        result = 0
        for i in range(n):
            if not visited[i]:
                sizeOfComponent = self.dfs(i, adj, visited)
                result += sizeOfComponent * (remainingNodes - sizeOfComponent)
                remainingNodes -= sizeOfComponent
        return result
