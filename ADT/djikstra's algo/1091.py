# Google, Meta, Microsoft, Amazon

# Using BFS
# No different weight, that's why bfs will work
from collections import deque


class Solution:
    directions = [(1, 1), (0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (1, -1), (-1, 1)]

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == 0 or n == 0 or grid[0][0] != 0:
            return -1

        que = deque([(0, 0)])
        grid[0][0] = 1

        def isSafe(x, y):
            return 0 <= x < m and 0 <= y < n

        steps = 1

        while que:
            N = len(que)
            for _ in range(N):
                x, y = que.popleft()

                if x == m - 1 and y == n - 1:
                    return steps

                for dx, dy in self.directions:
                    x_ = x + dx
                    y_ = y + dy

                    if isSafe(x_, y_) and grid[x_][y_] == 0:
                        que.append((x_, y_))
                        grid[x_][y_] = 1
            steps += 1
        return -1


# Using Dijikstra's Algo

from heapq import heappush, heappop
from math import inf


class Solution:
    def __init__(self):
        self.directions = [
            (1, 1),
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
            (-1, -1),
            (1, -1),
            (-1, 1),
        ]

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid)
        if m == 0 or n == 0 or grid[0][0] != 0:
            return -1

        def isSafe(x, y):
            return 0 <= x < m and 0 <= y < n

        result = [[inf] * n for _ in range(m)]
        pq = []
        heappush(pq, (0, (0, 0)))
        result[0][0] = 0

        while pq:
            d, (x, y) = heappop(pq)

            for dx, dy in self.directions:
                x_ = x + dx
                y_ = y + dy
                dist = 1

                if isSafe(x_, y_) and grid[x_][y_] == 0 and d + dist < result[x_][y_]:
                    heappush(pq, (d + dist, (x_, y_)))
                    grid[x_][y_] = 1
                    result[x_][y_] = d + dist

        return -1 if result[m - 1][n - 1] == inf else result[m - 1][n - 1] + 1
