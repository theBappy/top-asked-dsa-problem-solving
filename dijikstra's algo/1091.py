#  Google, Meta, Microsoft, Amazon
# BFS(Shortest Path)
# Dijkstra' Algorithm(Src to Destination shortest path) => 2D Matrix
# Tc = O(m.n) [rows.cols]
# Sc = o(m.n)
from collections import deque
from typing import List, Tuple

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m == 0 or n == 0 or grid[0][0] != 0:
            return -1

        directions = [(1, 1), (0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (1, -1), (-1, 1)]
        
        def is_safe(x: int, y: int) -> bool:
            return 0 <= x < m and 0 <= y < n
        
        result = [[float('inf')] * n for _ in range(m)]
        pq = deque()
        
        pq.append((0, 0, 0))  # (distance, x, y)
        result[0][0] = 0
        
        while pq:
            d, x, y = pq.popleft()
            
            for dx, dy in directions:
                x_ = x + dx
                y_ = y + dy
                dist = 1

                if is_safe(x_, y_) and grid[x_][y_] == 0 and d + dist < result[x_][y_]:
                    pq.append((d + dist, x_, y_))
                    grid[x_][y_] = 1  # Mark as visited
                    result[x_][y_] = d + dist
        
        if result[m - 1][n - 1] == float('inf'):
            return -1
        
        return result[m - 1][n - 1] + 1

        
