class Solution {
  public:
    vector<int> bellmanFord(int V, vector<vector<int>>& edges, int src) {
        vector<int> result(V, 1e8); // Use V instead of v
        result[src] = 0;

        for(int count = 1; count <= V - 1; count++) { // Fix typo from connt to count // V-1 times run
            for(auto &edge: edges) { // E times run
                int u = edge[0];
                int v = edge[1];
                int w = edge[2];
                if(result[u] != 1e8 && result[u] + w < result[v]) {
                    result[v] = result[u] + w;
                }
            }
        }

        // Cycle detection
        for(auto &edge: edges) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];
            if(result[u] != 1e8 && result[u] + w < result[v]) {
                return vector<int>{-1}; // Correct return statement
            }
        }
        return result;
    }
};
