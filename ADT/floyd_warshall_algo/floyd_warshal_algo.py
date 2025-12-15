class Solution:
    def shortest_distance(self, grid):
        n = len(grid)
        INF = 10**5

        # Step 1: Replace -1 with INF and fix diagonal
        for i in range(n):
            for j in range(n):
                if grid[i][j] == -1:
                    grid[i][j] = INF
            grid[i][i] = 0  # Distance to itself is 0

        # Step 2: Floyd–Warshall
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if grid[i][via] < INF and grid[via][j] < INF:
                        grid[i][j] = min(
                            grid[i][j],
                            grid[i][via] + grid[via][j]
                        )

        # Step 3: Negative cycle detection
        # If distance from a node to itself becomes negative,
        # then a negative cycle exists
        for i in range(n):
            if grid[i][i] < 0:
                return [-1]  # Negative cycle detected

        # Step 4: Convert INF back to -1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == INF:
                    grid[i][j] = -1

        return grid
