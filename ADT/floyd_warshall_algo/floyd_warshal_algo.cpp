// Samsung
//Time Complexity - O(n^3)
// Sc = O(1)

class Solution {
  public:
    void shortest_distance(vector<vector<int>>& grid) {
        int n = grid.size();
        const int INF = 100000;

        // Step 1: Replace -1 with INF and fix diagonal
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == -1)
                    grid[i][j] = INF;
            }
            grid[i][i] = 0;  // distance to self is always 0
        }

        // Step 2: Floyd–Warshall
        for (int via = 0; via < n; via++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {

                    // Only update if both paths exist
                    if (grid[i][via] < INF && grid[via][j] < INF) {
                        grid[i][j] = min(
                            grid[i][j],
                            grid[i][via] + grid[via][j]
                        );
                    }
                }
            }
        }

        // Step 3: Convert INF back to -1
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == INF)
                    grid[i][j] = -1;
            }
        }
    }
};
