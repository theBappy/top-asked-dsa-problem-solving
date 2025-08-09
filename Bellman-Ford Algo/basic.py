# Tc = O(V.E) [outer loops V - 1 times run, inner loops E times run]
# Sc = O(V + E) [result vector for V vertices, storage for edges]
# In Dijkstra Tc, O(E.logV) < Bellman Ford O(V.E)

class Solution:
    def bellmanFord(self, V, edges, src):
        # Initialize distances from src to all other vertices as infinite
        result = [float('inf')] * V
        result[src] = 0

        # Relax all edges |V| - 1 times
        for count in range(V - 1):
            for u, v, w in edges:
                if result[u] != float('inf') and result[u] + w < result[v]:
                    result[v] = result[u] + w

        # Check for negative weight cycles
        for u, v, w in edges:
            if result[u] != float('inf') and result[u] + w < result[v]:
                return [-1]  # Return -1 if a negative cycle is detected

        return result
