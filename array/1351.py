# Amazon

from bisect import bisect_right
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = 0
        for row in grid:
            idx = bisect_right(row, 0, key=lambda x: -x)
            result += n - idx
        return result

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        row = m - 1
        col = 0
        result = 0
        while row >= 0 and col < n:
            if grid[row][col] < 0:
                result += n - col
                row -= 1
            else:
                col += 1
        return result

