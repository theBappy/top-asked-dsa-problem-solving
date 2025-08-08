# Shortest Path(0 to n-1)
# Dijkstra's Algorithm
# But in this problem it's double ended dijkstra's algo(src->destination, destination->src)
# Tc = O(V+E).logV
# Sc = pq => O(V+E)

class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(n)]
        for u, v, w in edges: 
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        def fn(source): 
            dist = [inf]*n
            dist[source] = 0 
            pq = [(0, source)]
            while pq: 
                x, u = heappop(pq)
                if dist[u] == x: 
                    for v, w in graph[u]: 
                        if x+w < dist[v]: 
                            dist[v] = x+w
                            heappush(pq, (x+w, v))
            return dist 
        
        dist0, dist1 = fn(0), fn(n-1)
        return [dist0[n-1] < inf and (dist0[u] + w + dist1[v] == dist0[n-1] or dist0[v] + w + dist1[u] == dist0[n-1]) for u, v, w in edges]






import heapq
from collections import defaultdict
from typing import List, Tuple

class Solution:
    def dijkstra(self, adj: defaultdict[int, List[Tuple[int, int]]], src: int, n: int) -> List[int]:
        pq = []
        dist = [float('inf')] * n
        visited = [False] * n
        
        dist[src] = 0
        heapq.heappush(pq, (0, src))
        
        while pq:
            currWt, currNode = heapq.heappop(pq)
            
            if visited[currNode]:
                continue
            
            for nextNode, nextWt in adj[currNode]:
                if dist[nextNode] > currWt + nextWt:
                    dist[nextNode] = currWt + nextWt
                    heapq.heappush(pq, (currWt + nextWt, nextNode))
            
            visited[currNode] = True
        
        return dist
    
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        E = len(edges)
        adj = defaultdict(list)
        
        for edge in edges:
            u, v, w = edge
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        fromSrc = self.dijkstra(adj, 0, n)
        fromDest = self.dijkstra(adj, n - 1, n)
        
        result = [False] * E
        
        for i in range(E):
            u, v, w = edges[i]
            
            distFromSrc = fromSrc[u]
            distFromDest = fromDest[v]
            
            if distFromSrc + w + distFromDest == fromSrc[n - 1]:
                result[i] = True
            
            distFromSrc = fromSrc[v]
            distFromDest = fromDest[u]
            if distFromSrc + w + distFromDest == fromSrc[n - 1]:
                result[i] = True
        
        return result

          

