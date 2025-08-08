# Src = 0,0; destination = m-1, n-1
# 0,1 -> 0,2; cost = abs[grid[0][1] - grid[0][2]]
# Minimum path needs so Dijkstra's Algo not bfs bkz all weights are not equal
# Tc = O(log(m.n)) [This is because we are using a priority queue (min-heap) to process each cell, and in the worst case, we may need to push and pop each cell from the priority queue, which takes-> log(m.n) time for each operation]
# Sc = O(m.n) [result grid]

import heapq

class Solution:
    def minimumEffortPath(self, heights):
        m, n = len(heights), len(heights[0])
        
        def is_safe(x, y):
            return 0 <= x < m and 0 <= y < n
        
        result = [[float('inf')] * n for _ in range(m)]
        pq = []
        
        heapq.heappush(pq, (0, (0, 0)))
        result[0][0] = 0
        
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        
        while pq:
            diff, (x, y) = heapq.heappop(pq)

            if x == m - 1 and y == n - 1:
                return diff
            
            for dir in directions:
                x_, y_ = x + dir[0], y + dir[1]

                if is_safe(x_, y_):
                    new_diff = max(diff, abs(heights[x][y] - heights[x_][y_]))
                    if result[x_][y_] > new_diff:
                        result[x_][y_] = new_diff
                        heapq.heappush(pq, (result[x_][y_], (x_, y_)))
        
        return result[m - 1][n - 1]

