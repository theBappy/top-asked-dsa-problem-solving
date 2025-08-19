# Google, Microsoft
# Only can go Right and Down
# When Column = n-1 we can only go down
# And Row = m-1 we can only go right
# With those two conditions we can go both right or down, then we will return the minimum as result from them
# Tc = O(m.n) [without memoization 2^m*n as have two options so 2^k, with memoization we are visiting only once]
# Sc = O(m.n)

# Recursion + Memoization
class Solution:
    def __init__(self):
        self.t = [[-1] * 201 for _ in range(201)]


    def solve(self, grid, i, j, m, n):
        if i == m - 1 and j == n - 1:
            self.t[i][j] = grid[i][j]  # Corrected assignment
            return self.t[i][j]
        if self.t[i][j] != -1:
            return self.t[i][j]
        if i == m - 1:  # we can only go right
            self.t[i][j] = grid[i][j] + self.solve(
                grid, i, j + 1, m, n
            )  # Corrected assignment
            return self.t[i][j]
        elif j == n - 1:  # we can go only down
            self.t[i][j] = grid[i][j] + self.solve(
                grid, i + 1, j, m, n
            )  # Corrected assignment
            return self.t[i][j]
        else:
            self.t[i][j] = grid[i][j] + min(
                self.solve(grid, i + 1, j, m, n), self.solve(grid, i, j + 1, m, n)
            )  # Corrected assignment
            return self.t[i][j]

    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        return self.solve(grid, 0, 0, m, n)

# Bottom Up
# State define: t[i][j] = minimum sum to reach till [i][j] from 0, 0

class Solution:
    def minPathSum(self, grid):
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        t = [[0] * n for _ in range(m)]
        
        t[0][0] = grid[0][0]
        
        for i in range(1, m):
            t[i][0] = t[i-1][0] + grid[i][0]
        
        for j in range(1, n):
            t[0][j] = t[0][j-1] + grid[0][j]
        
        for i in range(1, m):
            for j in range(1, n):
                t[i][j] = grid[i][j] + min(t[i-1][j], t[i][j-1])
        
        return t[m-1][n-1]





class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        t = [0] * n
        t[0] = grid[0][0]
        for j in range(1, n):
            t[j] = t[j-1] + grid[0][j]
        for i in range(1, m):
            t[0] += grid[i][0]
            for j in range(1, n):
                t[j] = grid[i][j] + min(t[j], t[j-1])
        return t[n-1]



