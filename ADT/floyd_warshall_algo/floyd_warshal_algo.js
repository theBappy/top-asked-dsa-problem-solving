class Solution {
    shortest_distance(grid) {
        const n = grid.length;
        const INF = 100000;

        // Step 1: Replace -1 with INF and fix diagonal
        for (let i = 0; i < n; i++) {
            for (let j = 0; j < n; j++) {
                if (grid[i][j] === -1) {
                    grid[i][j] = INF;
                }
            }
            grid[i][i] = 0; // Distance to itself is 0
        }

        // Step 2: Floyd–Warshall
        for (let via = 0; via < n; via++) {
            for (let i = 0; i < n; i++) {
                for (let j = 0; j < n; j++) {
                    if (grid[i][via] < INF && grid[via][j] < INF) {
                        grid[i][j] = Math.min(
                            grid[i][j],
                            grid[i][via] + grid[via][j]
                        );
                    }
                }
            }
        }

        // Step 3: Negative cycle detection
        for (let i = 0; i < n; i++) {
            if (grid[i][i] < 0) {
                return [-1]; // Negative cycle detected
            }
        }

        // Step 4: Convert INF back to -1
        for (let i = 0; i < n; i++) {
            for (let j = 0; j < n; j++) {
                if (grid[i][j] === INF) {
                    grid[i][j] = -1;
                }
            }
        }

        return grid;
    }
}
