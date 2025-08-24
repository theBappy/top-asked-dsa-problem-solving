# Microsoft, Abode
# DFS + Memoization
# Tc = O(m*n)
# Sc = O(m*n)

class Solution:
    def countPaths(self, grid):
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        t = [[-1] * n for _ in range(m)]

        def isSafe(i, j):
            return 0 <= i < m and 0 <= j < n

        def dfs(i, j):
            if t[i][j] != -1:
                return t[i][j]
            
            answer = 1  # Count the current cell
            for dir in directions:
                i_, j_ = i + dir[0], j + dir[1]
                if isSafe(i_, j_) and grid[i_][j_] < grid[i][j]:
                    answer = (answer + dfs(i_, j_)) % MOD
            
            t[i][j] = answer
            return answer

        result = 0
        for i in range(m):
            for j in range(n):
                result = (result + dfs(i, j)) % MOD
        
        return result
