import heapq
from typing import List, Tuple, Dict

class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.N = n
        self.adj: Dict[int, List[Tuple[int, int]]] = {}
        for edge in edges:
            u, v, cost = edge
            if u not in self.adj:
                self.adj[u] = []
            self.adj[u].append((v, cost))
        self.pq: List[Tuple[int, int]] = []

    def addEdge(self, edge: List[int]):
        u, v, cost = edge
        if u not in self.adj:
            self.adj[u] = []
        self.adj[u].append((v, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        result = [float('inf')] * self.N
        result[node1] = 0
        self.pq = [(0, node1)]
        heapq.heapify(self.pq)

        while self.pq:
            d, node = heapq.heappop(self.pq)
            if d > result[node]:
                continue
            for adjNode, dist in self.adj.get(node, []):
                if d + dist < result[adjNode]:
                    result[adjNode] = d + dist
                    heapq.heappush(self.pq, (d + dist, adjNode))

        return -1 if result[node2] == float('inf') else result[node2]
        