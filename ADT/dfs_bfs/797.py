# Directed Acyclic Graph(DAG)
# Amzaon, Microsoft

# DFS + Backtracking
# Tc = O(V+E)

class Solution:
    def dfs(
        self,
        graph: List[List[int]],
        u: int,
        target: int,
        result: List[List[int]],
        temp: List[int],
    ) -> None:
        temp.append(u)
        if u == target:
            result.append(temp[:])
        else:
            for v in graph[u]:
                self.dfs(graph, v, target, result, temp)
        temp.pop()

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        source = 0
        target = n - 1
        result = []
        temp = []
        self.dfs(graph, source, target, result, temp)
        return result

