# Dijkstra's Algorithm
# Flipkart, Microsoft
# Tc = O(V+E).logV
# Sc = O(V)
# Why not queue? multiple time update happens, that's why priority queue is more better

import heapq
from typing import List, Tuple

class Solution:
    def dijkstra(self, V: int, edges: List[List[int]], src: int) -> List[int]:
        # Create an adjacency list
        adj = [[] for _ in range(V)]
        for edge in edges:
            u, v, weight = edge
            adj[u].append((v, weight))
            adj[v].append((u, weight))
        pq = []
        result = [float('inf')] * V
        result[src] = 0
        heapq.heappush(pq, (0, src))
        while pq:
            d, node = heapq.heappop(pq)
            if d > result[node]:
                continue
            for adjNode, wt in adj[node]:
                if d + wt < result[adjNode]:
                    result[adjNode] = d + wt
                    heapq.heappush(pq, (result[adjNode]))
        return result

# using set 
import heapq
from typing import List
def dijkstra(self, V, edges, src):
    adj = [[] for _ in range(V)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    dist = [float('inf')] * V
    dist[src] = 0
    st = set()
    st.add((0, src))
    while st:
        d, node = min(st)
        st.remove((d, node))
        for neighbor, weight in adj[node]:
            if d + weight < dist[neighbor]:
                if dist[neighbor] != float('inf'):
                    st.discard(dist[neighbor], neighbor)
                dist[neighbor] = d + weight
                st.add((dist[neighbor], neighbor))
    return dist
