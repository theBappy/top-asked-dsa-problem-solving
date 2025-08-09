
from typing import List
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        spm = [[float('inf')] * n for _ in range(n)]
        
        for i in range(n):
            spm[i][i] = 0

        for u, v, wt in edges:
            spm[u][v] = min(spm[u][v], wt)
            spm[v][u] = min(spm[v][u], wt)
            
        # Floyd-Warshall
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if spm[i][k] + spm[k][j] < spm[i][j]:
                        spm[i][j] = spm[i][k] + spm[k][j]

        min_reachable = float('inf')
        result_city = -1
        
        for i in range(n):
            reachable = sum(1 for j in range(n) if i != j and spm[i][j] <= distanceThreshold)
            
            if reachable < min_reachable:
                min_reachable = reachable
                result_city = i
            elif reachable == min_reachable and i > result_city:
                result_city = i

        return result_city


