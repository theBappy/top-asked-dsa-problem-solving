# Google, Meta


# DFS + Binary Search
class Solution:
    def __init__(self):
        self.ROW = 0
        self.COL = 0
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def DFS(self, grid: List[List[int]], i: int, j: int) -> bool:
        if i < 0 or i >= self.ROW or j < 0 or j >= self.COL or grid[i][j] == 1:
            return False
        if i == self.ROW - 1:
            return True
        grid[i][j] = 1
        for di, dj in self.directions:
            new_i, new_j = i + di, j + dj
            if self.DFS(grid, new_i, new_j):
                return True
        return False

    def canCross(self, cells: List[List[int]], mid: int) -> bool:
        grid = [[0] * self.COL for _ in range(self.ROW)]
        for i in range(mid + 1):
            x, y = cells[i][0] - 1, cells[i][1] - 1
            grid[x][y] = 1
        for j in range(self.COL):
            if grid[0][j] == 0 and self.DFS(grid, 0, j):
                return True
        return False

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        self.ROW = row
        self.COL = col
        l, r = 0, len(cells) - 1
        lastDay = 0
        while l <= r:
            mid = l + (r - l) // 2
            if self.canCross(cells, mid):
                lastDay = mid + 1
                l = mid + 1
            else:
                r = mid - 1
        return lastDay


# BFS + Binary Search
from collections import deque


class Solution:
    def __init__(self):
        self.ROW = 0
        self.COL = 0
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def BFS(self, grid: List[List[int]], i: int, j: int) -> bool:
        que = deque()
        que.append((i, j))
        grid[i][j] = 1
        while que:
            x, y = que.popleft()
            if x == self.ROW - 1:
                return True
            for dir_x, dir_y in self.directions:
                new_x = x + dir_x
                new_y = y + dir_y
                if (
                    0 <= new_x < self.ROW
                    and 0 <= new_y < self.COL
                    and grid[new_x][new_y] == 0
                ):
                    que.append((new_x, new_y))
                    grid[new_x][new_y] = 1
        return False

    def canCross(self, cells: List[List[int]], mid: int) -> bool:
        grid = [[0] * self.COL for _ in range(self.ROW)]
        for i in range(mid + 1):
            x, y = cells[i][0] - 1, cells[i][1] - 1
            grid[x][y] = 1
        for j in range(self.COL):
            if grid[0][j] == 0 and self.BFS(grid, 0, j):
                return True
        return False

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        self.ROW = row
        self.COL = col
        l, r = 0, len(cells) - 1
        lastDay = 0
        while l <= r:
            mid = l + (r - l) // 2
            if self.canCross(cells, mid):
                lastDay = mid + 1
                l = mid + 1
            else:
                r = mid - 1
        return lastDay
