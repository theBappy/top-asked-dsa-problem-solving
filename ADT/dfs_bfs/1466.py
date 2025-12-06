# Meta

from collections import defaultdict


class Solution:
    def __init__(self):
        self.edgesToReverse = 0

    def dfs(self, curr, parent, adj):
        for nextNode, isOutgoingFromOriginal in adj[curr]:
            if nextNode != parent:
                if isOutgoingFromOriginal == 1:
                    self.edgesToReverse += 1
                self.dfs(nextNode, curr, adj)

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in connections:
            adj[a].append((b, 1))
            adj[b].append((a, 0))
        self.dfs(0, -1, adj)
        return self.edgesToReverse
