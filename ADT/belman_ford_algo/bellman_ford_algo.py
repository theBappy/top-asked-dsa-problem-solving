from typing import List

class Solution:
    def bellman_ford(self, V: int, edges: List[List[int]], src: int) -> List[int]:
        INF = 10**8

        # Step 1: Initialize distance array
        dist = [INF] * V
        dist[src] = 0

        # Step 2: Relax all edges V-1 times
        for _ in range(V - 1):
            updated = False

            for u, v, w in edges:
                # Relax edge only if u is reachable
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True

            # Optimization: stop early if no update happened
            if not updated:
                break

        # Step 3: Check for negative weight cycle
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                return [-1]  # Negative cycle detected

        return dist
