#  Tc = O(E.logV)
#  Sc = O(V+E)
import heapq

class Solution:
    def primsAlgo(self, adj, V):
        pq = []
        heapq.heappush(pq, (0, 0))  # (weight, node)
        in_mst = [False] * V
        sum = 0
        
        while pq:
            wt, node = heapq.heappop(pq)
            
            if in_mst[node]:
                continue
                
            in_mst[node] = True
            sum += wt
            
            for neighbor, neighbor_wt in adj[node]:
                if not in_mst[neighbor]:
                    heapq.heappush(pq, (neighbor_wt, neighbor))
        
        return sum
    
    def minCostConnectPoints(self, points):
        V = len(points)
        adj = [[] for _ in range(V)]
        
        for i in range(V):
            for j in range(i+1, V):
                x1, y1 = points[i]
                x2, y2 = points[j]
                d = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((j, d))
                adj[j].append((i, d))
                
        return self.primsAlgo(adj, V)
