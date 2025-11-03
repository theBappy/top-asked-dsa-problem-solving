from typing import List

class Solution:
    def mark_guarded(self, row: int, col: int, grid: List[List[int]]) -> None:
        for i in range(row - 1, -1, -1):
            if grid[i][col] == 2 or grid[i][col] == 3:
                break
            grid[i][col] = 1
        for i in range(row + 1, len(grid)):
            if grid[i][col] == 2 or grid[i][col] == 3:
                break
            grid[i][col] = 1
        for j in range(col - 1, -1, -1):
            if grid[row][j] == 2 or grid[row][j] == 3:
                break
            grid[row][j] = 1
        for j in range(col + 1, len(grid[0])):
            if grid[row][j] == 2 or grid[row][j] == 3:
                break
            grid[row][j] = 1

    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        grid = [[0] * n for _ in range(m)]
        for i, j in guards:
            grid[i][j] = 2
        for i, j in walls:
            grid[i][j] = 3
        for i, j in guards:
            self.mark_guarded(i, j, grid)
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1

        return count
