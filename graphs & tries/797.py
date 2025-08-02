# Amazon, Microsoft
# Directed Cyclic Graph(DAG)
# Tc = O(n)
# Sc = O(n)
class Solution:
    def dfs(self, graph, u, target, result, temp):
        temp.append(u)
        if u == target:
            result.append(temp[:])
        else:
            for v in graph[u]:
                self.dfs(graph, v, target, result, temp)
        temp.pop()

    def allPathSourceTarget(self, graph):
        n = len(graph)
        source = 0
        target = n - 1
        result = []
        temp = []
        self.dfs(graph, source, target, result, temp)
        return result