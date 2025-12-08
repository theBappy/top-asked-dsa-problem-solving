class Solution:
    def __init__(self):
        self.result = -1

    def dfs(
        self,
        u: int,
        edges: List[int],
        visited: List[bool],
        count: List[int],
        inRecursion: List[bool],
    ):
        if u != -1:
            visited[u] = True
            inRecursion[u] = True
            v = edges[u]
            if v != -1 and not visited[v]:
                count[v] = count[u] + 1
                self.dfs(v, edges, visited, count, inRecursion)
            elif v != -1 and inRecursion[v]:
                self.result = max(self.result, count[u] - count[v] + 1)
            inRecursion[u] = False

    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        visited = [False] * n
        count = [1] * n
        inRecursion = [False] * n
        for i in range(n):
            if not visited[i]:
                self.dfs(i, edges, visited, count, inRecursion)
        return self.result
